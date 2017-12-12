from lxml import html
from lxml import etree
import requests

    page = requests.get('https://nips.cc/Conferences/2017/Schedule?type=Poster')
    tree = html.fromstring(page.content)
titles = tree.xpath('//div[@class="maincardBody"]/text()')
#titles_value = tree.xpath('//div[@onclick]/div/text()')
#print(titles_value)

#root = etree.parse('https://nips.cc/Conferences/2017/Schedule?type=Poster').getroot()

#for div in root.iterdescendants("div"):
    #cls = div.attrib.get("class")

tree.get()

for e in paper_numbers:
    print(e.attrib.get)

paper_numbers = tree.xpath('//div[@onclick]/div[@class="maincard narrower Poster"]/id')
element.get('attribute-name')
element.get('id')
                #tree.xpath('//h3[@data-analytics]/a/span/text()')
                #tree.xpath('//h3[@data-analytics]/a/@href')
#paper_numbers = tree.xpath('//div[@class="maincard narrower Poster"]/id/text()')
#paper_numbers = tree.xpath('//div[contains(@class, "maincard narrower Poster")]//id/value()')
#paper_numbers = tree.xpath('//div[@onclick]/div/id/text()')
print(paper_numbers)


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