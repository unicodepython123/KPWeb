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
    pattern = '<div class="row10"><a class="title1" href="(.*?)">.*?</a></div>'
    for link in hyperlink:
        print('**Vist link', link)
        print('...')
        html = requests.get(link).text
        PostLink =  re.findall(pattern, html)
    for i in range (0, len(PostLink)):
        PostLink[i] = 'https://baodaklak.vn/' + PostLink[i]
        html_post = requests.get(PostLink[i]).text
        file_name = re.sub(r'[\\/*?:"<>|]', "-", PostLink[i]) + ".html"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(html_post)                          


hyperLink = getLink(url)
getPostLink(hyperLink)


    
