import pandas as pd
import regex as re
import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('omw-1.4')
nltk.download('stopwords')


def format_na_values(df, default_date='2022-01-01'):
    """
    :param default_date:
    :param df: a dataframe
    :return: a dataframe with replacement of NaN values as either 0 for numeric fields, 'na' for text and False for bool
    """
    for f in df.columns:
        # integer
        if (df[f].dtype == "int") or (df[f].dtype == "int64") or (df[f].dtype == "float") or (df[f].dtype == "float64"):
            df[f] = df[f].fillna(0)

        # dates
        elif df[f].dtype == '<M8[ns]':
            df[f] = df[f].fillna(pd.to_datetime(default_date))

        # boolean
        elif df[f].dtype == 'bool':
            df[f] = df[f].fillna(True)

        # string
        else:
            df[f] = df[f].fillna('')

    return df


def pre_process(text):
    # lowercase
    text = text.lower()

    # remove tags
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

    # remove special characters and digits
    text = re.sub("(\\d|\\W)+", " ", text)

    # Convert to list from string
    text = text.split()

    # remove stopwords
    text = [word for word in text if word not in create_stopwords()]

    # remove words less than three letters
    text = [word for word in text if len(word) >= 3]

    # lemmatize
    lmtzr = WordNetLemmatizer()
    text = [lmtzr.lemmatize(word) for word in text]

    return ' '.join(text)


def create_stopwords():
    stop_words = set(stopwords.words('english'))

    # Creating a list of custom stopwords
    new_words = [

    ]

    return stop_words.union(new_words)
