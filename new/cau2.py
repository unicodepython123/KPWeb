import requests
from bs4 import BeautifulSoup
import re

url = 'https://vov.gov.vn/Rss/RssChuyende?pageSize=&chuyendeId=14'


def getLink(url):
    hyperlink = [url]
    for i in range (2,135):
        link = 'https://vov.gov.vn/Rss/RssChuyende?page='+str(i)+'&chuyendeId=14'
        hyperlink = hyperlink + [link]
    return hyperlink

def getPostLink(hyperlink):
    hyperPostLink = []
    pattern = '<div class="muc212-1"><a href="/(.*?)">.*?</a></div>'
    for link in hyperlink:
        print('**Vist link', link)
        print('...')
        html = requests.get(link).text
        PostLink =  re.findall(pattern, html)
        for i in range (0, len(PostLink)):
            PostLink[i] = 'https://vov.gov.vn/' + PostLink[i]
        hyperPostLink = hyperPostLink + [PostLink]
    return hyperPostLink

hyperLink = getLink(url)
hyperPostLink = getPostLink(hyperLink)
for i in range (0, len(hyperPostLink)):
    print ('trang', i + 1)
    for j in range (0, len(hyperPostLink[i])):
        print(hyperPostLink[i][j])
        print('')