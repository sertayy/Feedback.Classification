import string
import pickle
import pandas as pd
from nltk.tokenize import word_tokenize
from snowballstemmer import TurkishStemmer
turkStem = TurkishStemmer()


# Lowercase given text data
def lowercase_text(data):
    return data.lower()


# Remove whitespaces from given text data
def remove_whitespace(data):
    return " ".join(data.split())


# Remove punctuations from given text data
def remove_punctuations(data):
    return "".join([char for char in data if char not in string.punctuation])


# Stem the given text data
def stem_text(data):
    tokenized_data = word_tokenize(data)
    stemmed_data_list = turkStem.stemWords(tokenized_data)
    return " ".join(stemmed_data_list)


if __name__ == "__main__":
    with open("reviews_df_19_6.pickle", "rb") as p:
        reviews_df: pd.DataFrame = pickle.load(p)

    reviews_df["review"] = reviews_df["review"].apply(lowercase_text)
    reviews_df["review"] = reviews_df["review"].apply(remove_punctuations)
    reviews_df["review"] = reviews_df["review"].apply(remove_whitespace)
    # reviews_df["review"] = reviews_df["review"].apply(stem_text)
    with open("reviews_df_punc_23_6.pickle", "wb") as output_file:
        pickle.dump(reviews_df, output_file)
