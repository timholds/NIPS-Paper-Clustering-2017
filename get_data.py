from lxml import html
from lxml import etree
import requests
import re
import time

homepage = requests.get('https://nips.cc/Conferences/2017/Schedule?type=Poster')
tree = html.fromstring(homepage.content)
titles = tree.xpath('//div[@class="maincardBody"]/text()')

# Save the titles
with open('paper-titles.txt', 'w+') as f:
    for title in titles:
        f.write(title + '\n')


# Get info that will find the page with the paper's abstract
paper_numbers = tree.xpath('//div[@onclick]/div/@id')
links = []

for i in range(len(paper_numbers)):
    paper = paper_numbers[i]
    #paper_number = int(''.join(filter(str.isdigit, paper)))
    paper_number = re.findall(r'\d+', paper)

    for item in paper_number: # Since paper_number turns out to be a one item list
        # Make the new url and add it to the list of links
        link =  'https://nips.cc/Conferences/2017/Schedule?showEvent=' + item
        links.append(link)
        # Parse the paper's page to get the abstract
        paper_page = requests.get(link)
        tree_1 = html.fromstring(paper_page.content)
        abstracts_list = tree_1.xpath('//div[@class="abstractContainer"]/p/text()')
        #print(abstracts_list)
        time.sleep(.1)
#print(links)

#Save the links
with open('paper-links.txt', 'w+') as f:
    for paper in paper_numbers:
        f.write(paper + '\n')

# Save the abstracts
with open('paper-abstracts.txt', 'w+') as f:
    for abstract in abstracts_list:
        f.write(abstract + '\n')

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