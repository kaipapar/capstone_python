# Free Keyword Clustering
import pandas as pd
import re
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
import nltk
from nltk.stem.snowball import SnowballStemmer
snow_stemmer = SnowballStemmer(language='english')
from nltk.stem import PorterStemmer
porter_stemmer = PorterStemmer()
import csv
def stemmList(list):
    stemmed_list = []
    for l in list:
        words = l.split(" ")
        stem_words = []
        print(l)
        for word in words:
            x = snow_stemmer.stem(word)
            #x = porter_stemmer.stem(word)
            stem_words.append(x)
        key = " ".join(stem_words)
        print(key)
        stemmed_list.append(key)
    return stemmed_list
textlist = []
#queries.csv: your queries that should be clustered
df = pd.read_csv('output.csv', delimiter=';')
textlist = df.iloc[:, 0].to_list()
labellist = textlist
textlist = stemmList(textlist)

#-------------------------------------
LANGUAGE = 'english' # used for snowball stemmer
SENSITIVITY = 0.1 # The Lower the more clusters
MIN_CLUSTERSIZE = 2
tfidf_vectorizer = TfidfVectorizer(max_df=0.2, max_features=10000,min_df=0.01, stop_words=LANGUAGE,use_idf=True, ngram_range=(1,2))
tfidf_matrix = tfidf_vectorizer.fit_transform(textlist)
ds = DBSCAN(eps=SENSITIVITY, min_samples=MIN_CLUSTERSIZE).fit(tfidf_matrix)
clusters = ds.labels_.tolist()

cluster_df = pd.DataFrame(clusters, columns=['Cluster'])
keywords_df =  pd.DataFrame(labellist, columns=['Keyword'])
result = pd.merge(cluster_df, keywords_df, left_index=True, right_index=True)
grouping = result.groupby(['Cluster'])['Keyword'].apply(' | '.join).reset_index()
grouping.to_csv("clustered_queries.csv",index=False)