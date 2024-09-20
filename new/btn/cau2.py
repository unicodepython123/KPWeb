import requests
from bs4 import BeautifulSoup
import re

url = 'https://baodaklak.vn/khoa-hoc-cong-nghe/'


def getLink(url):
    hyperlink = [url]
    for i in range (2,168):
        link = 'https://baodaklak.vn/khoa-hoc-cong-nghe/?paged='+str(i)
        hyperlink = hyperlink + [link]
    return hyperlink

def getPostLink(hyperlink):
    hyperPostLink = []
    pattern = '<div class="row10"><a class="title1" href="(.*?)">.*?</a></div>'
    for link in hyperlink:
        print('**Vist link', link)
        print('...')
        html = requests.get(link).text
        PostLink =  re.findall(pattern, html)
        for i in range (0, len(PostLink)):
            PostLink[i] = 'https://baodaklak.vn/' + PostLink[i]
        hyperPostLink = hyperPostLink + [PostLink]
    return hyperPostLink

hyperLink = getLink(url)
hyperPostLink = getPostLink(hyperLink)
# for i in range (0, len(hyperPostLink)):
#     print ('trang', i + 1)
#     for j in range (0, len(hyperPostLink[i])):
#         print(hyperPostLink[i][j])
        

file_name = "cau2.txt"
with open(file_name, 'w', encoding='utf-8') as file:
    for i in range (0, len(hyperPostLink)):
        for j in range (0, len(hyperPostLink[i])):
            file.write(hyperPostLink[i][j] + '\n')
    
    
