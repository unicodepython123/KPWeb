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

def getPostContent(hyperlink):
    hyperPostContent = []
    for link in hyperlink:
        print('**Vist link', link)
        print('...')
        html = requests.get(link).text
        soup = BeautifulSoup(html, 'html5lib')
        title = soup.find_all('div', class_='muc212-1')
        summary = soup.find_all('div', class_='muc212-3')
        # time = soup.find_all('div', class_='muc212-2')
        # source = soup.find_all()
        str=""
        for i in range(len(title)):
            str+=title[i].text + "\n"
            str+="- " + summary[i].text + "\n"   
            # str+="- " + time[i].text + "\n"    
        hyperPostContent = hyperPostContent + [str]
    return hyperPostContent


hyperLink = getLink(url)
hyperPostContent = getPostContent(hyperLink)
print(hyperPostContent)