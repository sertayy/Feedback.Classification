"""## loading data for Turkish text classification
import pandas as pd
# https://www.kaggle.com/savasy/ttc4900
df=pd.read_csv("7allV03.csv")
df.columns=["labels","text"]
df.labels=pd.Categorical(df.labels)

traind_df=...
eval_df=...

# model
from simpletransformers.classification import ClassificationModel
import torch,sklearn

model_args = {
    "use_early_stopping": True,
    "early_stopping_delta": 0.01,
    "early_stopping_metric": "mcc",
    "early_stopping_metric_minimize": False,
    "early_stopping_patience": 5,
    "evaluate_during_training_steps": 1000,
    "fp16": False,
    "num_train_epochs":3
}

model = ClassificationModel(
    "bert",
    "dbmdz/bert-base-turkish-cased",
     use_cuda=cuda_available,
     args=model_args,
     num_labels=7
)
model.train_model(train_df, acc=sklearn.metrics.accuracy_score)"""