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
    links = []
    with open('paper-links.txt', 'r') as f:
        for line in f:
            line = f.readline()
            links.append(line)
    return links

# Get the abstracts from the web and save them to a text file
def get_paper_abstracts_from_web(links):
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
    #with open('paper-abstracts.txt', 'w+') as f:
        #f.writelines(abstract_list)
        # Save the links to a file

    # Save the abstracts
    with open('paper-abstracts.txt', 'w+') as f:
        for abstract in abstract_list:
            f.write(abstract+ '\n')
        # Since abstract_list is a list of lists
        #f.write(abstract_list)
        #for abstract in abstract_list:
        #f.writelines()
        #f.write([abstract] + '\n')

# Read the abstracts in from a txt file
def read_paper_abstracts_from_file():
    with open('paper-abstracts.txt', 'r') as f:
        abstracts = f.read()
    return abstracts

def get_data_from_web():
    #get_paper_titles_from_web()
    links = get_paper_links_from_web()
    get_paper_abstracts_from_web(links)

def get_data_from_txt():
    titles = read_paper_titles_from_file()
    abstracts = read_paper_abstracts_from_file()
    return [titles, abstracts]

if __name__ == '__main__':
    get_data_from_txt()

def run_all():
    get_data_from_web()
    get_data_from_txt()

#run_all()
