from __future__ import print_function
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem.snowball import SnowballStemmer
from bs4 import BeautifulSoup
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3

df_dirty = pd.read_csv('Papers-titles-abstracts.csv')
df_dirty = df_dirty.drop(['Unnamed: 0'], axis=1)
df = df_dirty[df_dirty['Abstracts'].notnull()]
print(df.shape)

titles = df.loc[:, 'Titles'].tolist()
abstracts = df.loc[:, 'Abstracts'].tolist()

# load nltk's English stopwords as variable called 'stopwords'
stopwords = nltk.corpus.stopwords.words('english')
stemmer = SnowballStemmer("english")

# Tokenizer and stemmer, which returns the set of stems in the text that it is passed

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

totalvocab_stemmed = []
totalvocab_tokenized = []
for i in abstracts:
    allwords_stemmed = tokenize_and_stem(i)
    totalvocab_stemmed.extend(allwords_stemmed)

    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index=totalvocab_stemmed)

# nltk.download('punkt')

for min in np.linspace(0.04, .2, num=16):
    print('The hyperparmeter for min_df is: ' + str(min))

    tfidf_vectorizer = TfidfVectorizer(max_df=.8, max_features=200000,
                               min_df=min, stop_words='english',
                               use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1, 3))

    tfidf_matrix = tfidf_vectorizer.fit_transform(abstracts)

    print(tfidf_matrix.shape)

    terms = tfidf_vectorizer.get_feature_names()
    print(terms)
    dist = 1 - cosine_similarity(tfidf_matrix)

    for i in range(1, 12):
        print('Number of clusters: ' + str(i))
        num_clusters = i
        km = KMeans(n_clusters=num_clusters)
        km.fit(tfidf_vectorizer.fit_transform(abstracts))
        clusters = km.labels_.tolist()
        print()
        print()
        order_centroids = km.cluster_centers_.argsort()[:, ::-1]
        # J up to 8 because any more than 8 words per category will become too overfitted
        for j in range(1, 8):
            print()
            print('-------------------------------')
            print()
            print('Number of clusters is: ' + str(num_clusters))
            print('Number of feature words per cluster: ' + str(j))
            print()
            #print('J equals: ' + str(j))
            for i in range(num_clusters):
                print()
                print("Cluster %d words:" % (i+1), end='')
                #print()
                #print()
                for ind in order_centroids[i, :j]:
                    print(' %s' % vocab_frame.loc[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
                    print()

# generates index for each item in the corpora (in this case it's just rank) and I'll use this for scoring later
ranks = []
for i in range(0, len(titles)):
    ranks.append(i)


papers = {'title': titles, 'rank': ranks, ' abstracts': abstracts, 'cluster': clusters}
# films = { 'title': titles, 'rank': ranks, 'synopsis': synopses, 'cluster': clusters, 'genre': genres }

frame = pd.DataFrame(papers, index=[clusters], columns=['rank', 'title', 'cluster'])
# frame = pd.DataFrame(films, index = [clusters] , columns = ['rank', 'title', 'cluster', 'genre'])


joblib.dump(km, 'doc_cluster.pkl')
km = joblib.load('doc_cluster.pkl')
clusters = km.labels_.tolist()


print("Top terms per cluster:")
print()

#order_centroids = km.cluster_centers_.argsort()[:, ::-1]
#num_clusters = 10

# Iterate through values of number of words per cluster
# Iterate through different numbers of clusters
# Picking 15 because
"""def run_the_jewels():
    for n in range(2, 15):
        print()
        print()
        num_clusters = n
        #order_centroids = km.cluster_centers_.argsort()[:, ::-1]
        # J because anything more than 12 seems excessive, diminishing returns
        for j in range(1, 12):
            print()
            print('-------------------------------')
            print()
            print('Number of clusters is: ' + str(n))
            print('Number of feature words per cluster: ' + str(j))
            print()
            #print('J equals: ' + str(j))
            for i in range(num_clusters):
                print()
                print("Cluster %d words:" % (i+1), end='')
                #print()
                #print()
                for ind in order_centroids[i, :j]:
                    print(' %s' % vocab_frame.loc[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
                    print()
                    #print()
"""