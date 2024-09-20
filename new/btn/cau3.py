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

def getPostContent(hyperlink):
    PostContentOfPage = []
    for link in hyperlink:
        print('**Vist link', link)
        print('...')
        html = requests.get(link).text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all('a', class_='title1')
        summary = soup.find_all('div', class_='des')
        # time = soup.find_all('div', class_='date|date row10')
        time = soup.find_all('div', class_=re.compile(r'date(\srow10)?'))
        # source = soup.find_all()
        # time = soup.select('div.date, div.date.row10')
        file_name = "cau3.txt"
        with open(file_name, 'a', encoding='utf-8') as file:
            for i in range (len(title)):
                file.write(title[i].text + '\n')
                file.write(f'- {summary[i].text}' + '\n')
                file.write(f'- {time[i].text}' + '\n')
    print("Đã cào xong")
          


hyperLink = getLink(url)
getPostContent(hyperLink)

        

# print(hyperPostContent)