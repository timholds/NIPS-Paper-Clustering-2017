from lxml import html
import requests
import re
import time

# Get the titles of all the papers
homepage = requests.get('https://nips.cc/Conferences/2017/Schedule?type=Poster')
tree = html.fromstring(homepage.content)
titles = tree.xpath('//div[@class="maincardBody"]/text()')

# Save the titles
with open('paper-titles.txt', 'w+') as f:
    for title in titles:
        f.write(title + '\n')


# Get the links to each paper's abstract page
paper_numbers = tree.xpath('//div[@onclick]/div/@id')
print(type(paper_numbers))
links = []
print(type(links))


for i in range(len(paper_numbers)):
    paper = paper_numbers[i]
    #paper_number = int(''.join(filter(str.isdigit, paper)))
    paper_number = re.findall(r'\d+', paper)

    for item in paper_number: # Since paper_number turns out to be a one item list
        # Make the new url and add it to the list of links
        link =  'https://nips.cc/Conferences/2017/Schedule?showEvent=' + item
        links.append(link)

#Save the links
with open('paper-links.txt', 'w+') as f:
    for link in links:
        f.write(link + '\n')

# Get the abstracts
abstract_list = []
for link in links:
    # Parse the paper's page to get the abstract
    paper_page = requests.get(link)
    tree_1 = html.fromstring(paper_page.content)
    abstract = tree_1.xpath('//div[@class="abstractContainer"]/p/text()')
    abstract_list.append(abstract)
    # print(abstracts_list)
    time.sleep(.1)


# Save the abstracts
with open('paper-abstracts.txt', 'w+') as f:
    for abstract in abstract_list:
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