from lxml import html
import requests
import re
import time

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
def read_paper_titles_from_file():
    with open('paper-titles.txt', 'r') as f:
        titles = f.read()
    return titles

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

    return links

# Read the links in from a txt file
def read_paper_links_from_file():
    with open('paper-links.txt', 'r') as f:
        links = f.read()
    return links

# Get the abstracts from the web and save them to a text file
def get_paper_abstracts_from_web(links):
    abstract_list = []
    for link in links:
        # Parse the paper's page to get the abstract
        paper_page = requests.get(link)
        tree_1 = html.fromstring(paper_page.content)
        abstract = tree_1.xpath('//div[@class="abstractContainer"]/p/text()')
        abstract_list.append(abstract)
        # print(abstracts_list)
        time.sleep(.01)

    print('abstract_list type is' + type(abstract_list))
    print((abstract_list))

    # Save the abstracts
    with open('paper-abstracts.txt', 'w+') as f:
        for abstract in abstract_list:
            print(type(abstract))
            f.write(abstract + '\n')

# Read the abstracts in from a txt file
def read_paper_abstracts_from_file():
    with open('paper-abstracts.txt', 'r') as f:
        abstracts = f.read()
    return abstracts

def get_data_from_web():
    get_paper_titles_from_web()
    links = get_paper_links_from_web()
    get_paper_abstracts_from_web(links)

def get_data_from_txt():
    titles = read_paper_titles_from_file()
    abstracts = read_paper_abstracts_from_file()
    return [titles, abstracts]

if __name__ == '__main__':
    get_data_from_txt()

#

#abstracts_df = pd.DataFrame(index=titles)
#print(abstracts_df)


# Get a list of links to abstracts
#for title in titles:
    #abstracts_df[paper] = abstract

"""
# For each paper, follow the link to the abstract and extract the abstract from that page
abstracts = tree.xpath('//div[@class="abstractContainer"]/text()')
with open('abstracts.txt', 'w+') as f:
    for abstract in abstracts:
        f.write(abstract + '\n')

print(titles)
"""