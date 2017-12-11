import pandas as pd
from paper_scrape import df2, titles, words_list_title

# Make a dataframe with paper ids (0-678) as the index, and paper titles as the first column
id_title_df = pd.DataFrame(titles, columns=['titles'])
#print(id_title_df)

# Returns the title at row i of the dataframe
for i in range(0, len(titles)):
    title = id_title_df.iloc[i]
#print(id_title_df.iloc[0])
print(words_list_title)

# Make a dataframe that stores the word in a column named word
word_ids_df = pd.DataFrame(words_list_title, columns=['word'])
#word_ids_df.set_index(['ids'])
# Add a new column and fill this in with the paper ids whose titles have the keyword
    # For a given word, go through all titles and record id of those titles with the word
    #for word in word_ids_df['word']:
        #word_ids_df[word]['ids'] = id

#word_ids_df['e'] = pd.Series(np.random.randn(sLength), index=df1.index)
#word_ids_df = word_ids_df.assign(ids=p.Series(np.random.randn(sLength)).values)


#print(word_ids_df)

#words_papers_dict = {}
#keywords = df2.index
#print(keywords)

# Given a title, get that papers id


#df = pd.DataFrame(index=[i for i in range(0, len(titles))], columns = [])

"""
for i in range(0, len(keywords)):
    for j in range((i+1), len(keywords)):
        # For the two keywords, get a list of the papers with that keyword
        word1_ids = df['ids'].iloc[i]
        word2_ids = df['ids'].iloc[j]
        word1 = df.iloc[i].index
        word2 = df.iloc[j].index
        print(word1)
        # Get papers whose titles contain the overlap of these keywords
        union = [id for id in word1_ids if id in word2_ids]
"""