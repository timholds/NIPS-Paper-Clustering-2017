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

# Get all of the words from each title

# Find the most common words

# Plot the most common words

# Extract the keywords from the title
# Make a dictionary with title as key and keywords as value

# Cluster the titles based on keywords

# Plot the clusters
