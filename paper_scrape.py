from lxml import html
import requests
import matplotlib as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import itertools


page = requests.get('https://nips.cc/Conferences/2017/Schedule?type=Poster')
tree = html.fromstring(page.content)

#posters = tree.xpath('//div[@class="maincard narrower Poster"]/text()')
titles = tree.xpath('//div[@class="maincardBody"]/text()')

#print('Posters: ', posters)
#print('Titles: ', titles)
print(len(titles))
for title in titles:
    words = title.split(" ")
    print(words)


def word_counter(df1):
    word_count = {}
    for word in title:
        # Special case if we're seeing this word for the first time.
        if not word in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1
    return word_count


# Function to plot hourly frequently viwordd webwords with the dataframe of words and times
def plot_words(df1):
    # List of every word with no repeats
    words = df1['page']
    word_count = word_counter(df1)
    word_series = sort_by_least_popular(word_count)
    return word_series


# Funciton that sorts webwords from least to most viwordd as measured by page visits
def sort_by_least_popular(word_count):
    word_count = pd.Series(
        word_count)
    word_count = pd.Series.sort_values(word_count)
    return word_count


# Function to plot the top 20 words
def plot_top_words():
    fig, ax = plt.subplots()
    pos = np.arange(20) + .5  # the bar centers on the y axis
    ax.barh(pos, word_series[-20:].values, align='center', fc='#80d0f1', ec='w')
    ax.set_xlabel("Site Visits Between January and November 2016")
    ax.set_yticks(pos)
    k = word_series[-20:].index
    ax.set_yticklabels(k)
    ax.set_title("Top Sites")
    return plt.tight_layout()

word_count = word_counter(df1)
word_series = sort_by_least_popular(word_count)
print("Plotting Top 20 Words")
plot_top_words()


# Get all of the words from each title

# Find the most common words

# Plot the most common words

# Extract the keywords from the title
# Make a dictionary with title as key and keywords as value

# Cluster the titles based on keywords

# Plot the clusters
