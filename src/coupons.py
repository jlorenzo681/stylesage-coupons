
import pandas as pd
import json
import pke
import spacy
import streamlit as st

from utils import format_na_values, pre_process


spacy.load("en_core_web_sm")

with open('src/coupons.json') as data_file:
    data = json.load(data_file)

# Get nested field in json
df = pd.json_normalize(data, 'coupons')

# Drop unneeded columns
df.drop(["country_code", "coupon_webshop_name"], axis=1, inplace=True)

# Nan values cleaning
df = format_na_values(df)

# Stats percent_off & dollar_off
df_dollar_percent_off = df[(df['promotion_type'] == 'percent-off') | (df['promotion_type'] == 'dollar-off')]
# Show discounts grouped by retailer
df_retailer_discounts = \
    df_dollar_percent_off.groupby(['webshop_id', 'promotion_type', 'value'], as_index=False)['value'].count()
# Show min, max, mean
df_discounts_stats = \
    df_dollar_percent_off.groupby(['promotion_type'], as_index=False)['value'].agg(['mean', 'min', 'max'])

# Keyword extraction from title, description
keyword_headers = ['title', 'description']
df_keywords = pd.DataFrame(df, columns=keyword_headers)

df_keywords['title_clean'] = df_keywords['title'].apply(lambda x: pre_process(x))
df_keywords['description_clean'] = df_keywords['description'].apply(lambda x: pre_process(x))

# define the set of valid Part-of-Speeches
pos = {'NOUN', 'PROPN', 'ADJ'}

# 1. create a SingleRank extractor.
extractor = pke.unsupervised.SingleRank()

text = df_keywords['description_clean'].to_string() + df_keywords['title_clean'].to_string()

# 2. load the content of the document.
extractor.load_document(input=text,
                        language='en')

# 3. select the longest sequences of nouns and adjectives as candidates.
extractor.candidate_selection(pos=pos)

# 4. weight the candidates using the sum of their word's scores that are
#    computed using random walk. In the graph, nodes are words of
#    certain part-of-speech (nouns and adjectives) that are connected if
#    they occur in a window of 10 words.
extractor.candidate_weighting(window=10,
                              pos=pos)

# 5. get the 10-highest scored candidates as keyphrases
keywords = extractor.get_n_best(n=10)

json_keywords = json.dumps(keywords)


# Presentation with Streamlit
st.dataframe(df_retailer_discounts)

st.json(json_keywords)
