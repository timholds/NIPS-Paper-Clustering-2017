from lxml import html
import requests
import re
import pandas as pd
import numpy as np

# A dataframe to store the titles, links, and abstracts eventually
df = pd.DataFrame()

# Get the titles of all the papers and write them to a file
def get_paper_titles_from_web():
    homepage = requests.get('https://nips.cc/Conferences/2017/Schedule?type=Poster')
    tree = html.fromstring(homepage.content)
    titles = tree.xpath('//div[@class="maincardBody"]/text()')

    with open('paper-titles.txt', 'w+') as f:
        for title in titles:
            f.write(title + '\n')

    return titles

# Read the titles in from a txt file
def read_paper_titles_from_file(df):
    with open('paper-titles.txt', 'r') as f:
        titles = f.read().split('\n')
    print('Number of titles ' + str(len(titles)))
    df['Titles'] = titles[:679]
    return df

# Get the links to all the paper's individual pages and save the links to a file
def get_paper_links_from_web():
    homepage = requests.get('https://nips.cc/Conferences/2017/Schedule?type=Poster')
    tree = html.fromstring(homepage.content)
    paper_numbers = tree.xpath('//div[@onclick]/div/@id')

    # Create an empty list to store the links to each paper
    links = []
    for i in range(len(paper_numbers)):
        paper = paper_numbers[i]
        paper_number = re.findall(r'\d+', paper)

        # Use each paper number to generate the link to the paper's individual page
        for item in paper_number: # Since paper_number turns out to be a one item list
            # Make the new url and add it to the list of links
            link = 'https://nips.cc/Conferences/2017/Schedule?showEvent=' + item
            links.append(link)

    #Save the links to a file
    with open('paper-links.txt', 'w+') as f:
        for link in links:
            f.write(link + '\n')

    print('Number of links: ' + str(len(links)))
    return links

# Read the links in from a txt file
def read_paper_links_from_file(df):
    links = []

    with open('paper-links.txt') as f:
        #for line in f:
        link_list = f.readlines()
        for link in link_list:
            links.append(link)

    """
    with open('paper-links.txt') as f:
        for line in f:
            link = f.readline()
            links.append(link)
        #line = f.readline()
        #for count, line in enumerate(f):
        #line =
    """

        #print(line)
    print('Number of links is ' +str(len(links)))
    df['Links'] = links
    return df

# Get the abstracts from the web and save them to a text file
def get_paper_abstracts_from_web_old(links):
    # Store all of the abstracts in abstract_list
    abstract_list = []
    for link in links:
        print(link)
        # Try parsing the paper's page to get the abstract
        try:
            paper_page = requests.get(link)
            tree_1 = html.fromstring(paper_page.content)
            abstracts = tree_1.xpath('//div[@class="abstractContainer"]/p/text()')
            # Since abstracts should be a list of length 1
            for abstract in abstracts:
                abstract_list.append(abstract)
        except (requests.exceptions.MissingSchema):
            print('Missing link')
        #time.sleep(.01)

    # Save the abstracts
    with open('paper-abstracts.txt', 'w+') as f:
        for abstract in abstract_list:
            f.write(abstract+ '\n')

# TODO - for each row of dataframe: get a link, try scraping abstract, put in abstract column of the row
# Put each abstract into its respective place in the dataframe, where title, link, and abstract for a paper are on one row
def get_paper_abstracts_from_web(df):
    print(df)

    df['Abstracts'] = np.nan
    # Get a series object of all the links to paper's URLs
    links = df.loc[:, 'Links']

    row = 0
    for link in iter(links):
        print(link)
        try:
            paper_page = requests.get(link)
            tree_1 = html.fromstring(paper_page.content)
            abstracts = tree_1.xpath('//div[@class="abstractContainer"]/p/text()')
            # Append the abstract list to that paper's row of the dataframe under 'Abstracts'
            for abstract in abstracts:
                print(abstract)
                df.loc[row, 'Abstracts'] = abstract
        except requests.exceptions.MissingSchema:
            print('Missing link')
            # Put -1 in that row of the dataframe under 'Abstracts'
            df.loc[row, 'Abstracts'] = 'None'
        row = row + 1
    df.to_csv('Papers-titles-abstracts.csv')
    return df

# TODO -decide if we want to get rid of this function and change the above to the name of this method
# Read the abstracts in from a txt file
# FIXME - issue is that there are less abstracts that titles, so when we read from file we
# dont know which abstract belongs to which title / which row of df
def read_paper_abstracts_from_file_():
    with open('paper-abstracts.txt', 'r') as f:
        abstracts = f.read().split('\n')
    print('Number of abstracts: ' + str(len(abstracts)))
    #for df['abstracts'] = abstracts
    return abstracts

def get_data_from_web():
    get_paper_titles_from_web()
    links = get_paper_links_from_web()
    get_paper_abstracts_from_web(links)

# Where do you use the links? Already used them in get_data_from_web, right?
def get_data_from_txt(df):
    titles = read_paper_titles_from_file(df)
    read_paper_links_from_file(df)
    get_paper_abstracts_from_web(df)
    return df

def run_all():
    get_data_from_web()
    get_data_from_txt()

get_data_from_txt(df)
#df.to_csv('Papers.csv')

# TODO FIXME - What Do I need to run to get a full dataframe to produce data? Put that into one file
#print(df)

#run_all()
#read_paper_titles_from_file(df)
#read_paper_links_from_file(df)
#read_paper_abstracts_from_file_to_df(df)
#get_paper_links_from_web()
