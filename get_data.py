from lxml import html
import requests
page = requests.get('https://nips.cc/Conferences/2017/Schedule?type=Poster')
tree = html.fromstring(page.content)
titles = tree.xpath('//div[@class="maincardBody"]/text()')
# Save the titles to a txt file
with open('paper-titles.txt', 'w+') as f:
    for title in titles:
        f.write(title + '\n')

print(titles)