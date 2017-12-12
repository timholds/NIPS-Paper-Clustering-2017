from lxml import html
from lxml import etree
import requests

page = requests.get('https://nips.cc/Conferences/2017/Schedule?type=Poster')
tree = html.fromstring(page.content)
titles = tree.xpath('//div[@class="maincardBody"]/text()')
paper_numbers = tree.xpath('//div[@onclick]/div/@id')

print(paper_numbers)

# For every poster, get the link to the poster page
for i in range(len(paper_numbers)):
    paper = paper_numbers[i]
    #paper_numbers = # Trim paper to just the number
    link =  'https://nips.cc/Conferences/2017/Schedule/showEvent=' + paper_number
    #print(link)

# Save the titles to a txt file
with open('paper-titles.txt', 'w+') as f:
    for title in titles:
        f.write(title + '\n')

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