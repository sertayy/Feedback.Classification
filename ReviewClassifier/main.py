import sys
import pandas as pd
import numpy as np
from pandas import DataFrame
from simpletransformers.classification import ClassificationModel
import sklearn
from sklearn import metrics
import os
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn import metrics
from read_helper import get_data_from_bigquery, read_json, read_config, read_csv
from preprocess_data import apply_preprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
K_FOLD = 5
DB_TYPE = "bigQuery"


def create_confisuon_matrix():
    array = [[74, 19, 14, 8],
             [40, 175, 37, 64],
             [6, 22, 65, 7],
             [5, 29, 9, 204]]
    df_cm = pd.DataFrame(array, index=[i for i in "BUFR"],
                         columns=[i for i in "BUFR"])
    plt.figure(figsize=(10, 7))
    sn.heatmap(df_cm, annot=True, fmt='g')
    plt.xlabel("true class")
    plt.ylabel("predicted class")
    metrics.classification_report()
    plt.show()


def train_model(df, k_fold_step):
    df = df.replace("bug report", 0) \
        .replace('feature request', 1) \
        .replace('ratings', 2) \
        .replace('user experience', 3) \
        .rename(columns={"review": "text", "category": "labels"})

    model_args = {
        "use_early_stopping": True,
        "early_stopping_delta": 0.01,
        "early_stopping_metric": "mcc",
        "early_stopping_metric_minimize": False,
        "early_stopping_patience": 5,
        "evaluate_during_training_steps": 1000,
        "fp16": False,
        "num_train_epochs": 3
    }

    model = ClassificationModel(
        "bert",
        "dbmdz/bert-base-turkish-cased",
        use_cuda=True,
        args=model_args,
        num_labels=4
    )
    model.train_model(df, acc=sklearn.metrics.accuracy_score, output_dir=k_fold_step)
    return model


def test_model(trained_model, test_df):
    labels_dict = {0: 'bug report', 1: 'feature request', 2: 'ratings', 3: 'user experience'}
    bug_predict = {
        "bug report": 0,
        "user experience": 0,
        "feature request": 0,
        "ratings": 0
    }
    ux_predict = {
        "bug report": 0,
        "user experience": 0,
        "feature request": 0,
        "ratings": 0
    }
    feature_predict = {
        "bug report": 0,
        "user experience": 0,
        "feature request": 0,
        "ratings": 0
    }
    rating_predict = {
        "bug report": 0,
        "user experience": 0,
        "feature request": 0,
        "ratings": 0
    }

    for index, row in test_df.iterrows():
        predictions = trained_model.predict(row["text"])[0]
        if row["labels"] == 0:
            bug_predict[labels_dict[predictions[0]]] += 1
        elif row["labels"] == 3:
            ux_predict[labels_dict[predictions[0]]] += 1
        elif row["labels"] == 1:
            feature_predict[labels_dict[predictions[0]]] += 1
        else:
            rating_predict[labels_dict[predictions[0]]] += 1

    print("Bug report predictions:\n"
          "\tbug report: {0}\n"
          "\tuser experience: {1}\n"
          "\tfeature request: {2}\n"
          "\tratings: {3}".format(bug_predict["bug report"], bug_predict["user experience"],
                                  bug_predict["feature request"], bug_predict["ratings"]))
    print("User experience predictions:\n"
          "\tbug report: {0}\n"
          "\tuser experience: {1}\n"
          "\tfeature request: {2}\n"
          "\tratings: {3}".format(ux_predict["bug report"], ux_predict["user experience"],
                                  ux_predict["feature request"], ux_predict["ratings"]))
    print("Feature request predictions:\n"
          "\tbug report: {0}\n"
          "\tuser experience: {1}\n"
          "\tfeature request: {2}\n"
          "\tratings: {3}".format(feature_predict["bug report"], feature_predict["user experience"],
                                  feature_predict["feature request"], feature_predict["ratings"]))
    print("Rating predictions:\n"
          "\tbug report: {0}\n"
          "\tuser experience: {1}\n"
          "\tfeature request: {2}\n"
          "\tratings: {3}".format(rating_predict["bug report"], rating_predict["user experience"],
                                  rating_predict["feature request"], rating_predict["ratings"]))


def k_fold(df: pd.DataFrame):
    df = df.sample(frac=1, random_state=1).reset_index(drop=True)
    categories = df['category'].unique()
    test_df = pd.DataFrame(columns=df.columns)
    train_df = pd.DataFrame(columns=df.columns)
    for i in range(K_FOLD):
        for category in categories:
            categ_df = df[df['category'] == category]
            categ_values = categ_df.values
            piece = int(len(categ_values) / K_FOLD)
            training = np.concatenate(
                (categ_values[:len(categ_values) - piece * (i+1), :], categ_values[len(categ_values) - piece*i, :]))
            test = categ_values[len(categ_values) - piece * (i+1):len(categ_values) - piece*i, :]
            train_df = train_df.append(DataFrame(training, columns=categ_df.columns), ignore_index=True)
            test_df = test_df.append(DataFrame(test, columns=categ_df.columns), ignore_index=True)
        trained_model = train_model(train_df, i)
        test_model(trained_model, test_df)


if __name__ == "__main__":
    df = None
    if os.path.exists(sys.argv[1]):
        file_path = sys.argv[1]
        config = read_config(sys.argv[1])
        if not config["is_file"] ^ config["db_connection"]:
            logger.error("is_file and db_connection parameters are not allowed to be same!")
        elif config["is_file"]:
            file_path = config["file_path"]
            file_extension = os.path.splitext(file_path)[1]
            if file_extension == ".json":
                df = read_json(file_path)
            elif file_extension == ".csv":
                df = read_csv(file_path)
            else:
                logger.error(f'File extension "{file_extension}" is not supported! Use .json or .csv files.')
        else:
            if config["db_type"] == DB_TYPE:
                df = get_data_from_bigquery(config)
            else:
                logger.error(f'"{config["db_type"]}" is not supported! Use "bigQuery" instead.')
        if df is not None:
            k_fold(df)
    else:
        logger.error(f'Input path {sys.argv[1]} does not exists!')
