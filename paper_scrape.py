from lxml import html
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

page = requests.get('https://nips.cc/Conferences/2017/Schedule?type=Poster')
tree = html.fromstring(page.content)
titles = tree.xpath('//div[@class="maincardBody"]/text()')

# For each title, split the title up into a list of lowercase words
words_list_title = []
for title in titles:
    words = title.split(" ")
    for word in words:
        word = word.lower()
        words_list_title.append(word)
    # The result is a bunch of lists, each representing a title
    #print(words_list_title)


# Count the frequency of word occurrences
word_count = {}
for word in words_list_title:
    if not word in word_count:
        word_count[word] = 1
    else:
        word_count[word] = word_count[word] + 1

df = pd.DataFrame.from_dict(word_count, orient='index')
df.columns = ['frequency']
df1 = df.sort_values(by='frequency', ascending=False)
#print(df1.head(50))

# Drop the rows of words like 'the' and 'of' that don't relate to the content of the paper
df2 = df1.drop(['for', 'of', 'with', 'and', 'in', 'a', 'the', 'to', 'on', 'from', 'via', 'using', 'by'], axis=0)
#print(df2.head(50))

plt.rcdefaults()
fig, ax = plt.subplots()
words_list = df2.index.tolist()
y_pos = np.arange(len(words_list))
frequency = df2['frequency']    
ax.barh(y_pos, frequency, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(words)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Number of Occurrences')
ax.set_title('Which Words are Used Most Frequently in Accepted Papers at NIPS 2017?')

plt.show()
plt.savefig('words-in-title-freq.jpg')







"""
plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
words = # get the first 10 words from the
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()



    # Get the dictionary as a list of tuples starting with words that have the highest frequency
#sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reversed=True)
#print(sorted_word_count)

    #for title in words_list_
    #words_list_all_titles.append(words_list_title)

#words = title.split(" ")
#print(words)
#uniqWords = sorted(set(words_list_all_titles)) #remove duplicate words and sort
#for word in uniqWords:
    #print(words_list_all_titles.count(word), word)
"""

"""
for title in titles:
    # Split each title into a list of words and make them all lowercase
    words = title.split(" ")
    words_list_title = []
    for word in words:
        word = word.lower()
        print(word)
        words_list_title.append(word)
    #print(words)
    #print(words_list)
words_list_all_titles = []
words_list_all_titles.append(words_list_title)
print(words_list_all_titles[0])

# Make a dict with the word as key and # of occurences as value
word_count = {}
for word in words_list_all_titles:
    if not word in word_count:
        word_count[word] = 1
    else:
        word_count[word] = word_count[word] + 1
print(word_count)
"""

"""
#def count_topics():
# Count the number of times a word is used over all the titles
def word_counter():
    for title in titles:
        words = title.split(" ").lower()
        # Store each word as a key in a dict, and update the value with how many times the word has occured
        word_count = {}
        for word in title:
            if not word in word_count:
                word_count[word] = 1
            else:
                word_count[word] = word_count[word] + 1
    print(word_count)
    return word_count

word_counter()
"""

"""
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
"""


# Get all of the words from each title

# Find the most common words

# Plot the most common words

# Extract the keywords from the title
# Make a dictionary with title as key and keywords as value

# Cluster the titles based on keywords

# Plot the clusters
