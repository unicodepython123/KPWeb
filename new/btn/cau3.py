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
    for link in hyperlink:
        print('**Vist link', link)
        print('...')
        html = requests.get(link).text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all('a', class_='title1')
        summary = soup.find_all('div', class_='des')
        # time = soup.find_all('div', class_='date|date row10')
        # time = soup.find_all('div', class_=re.compile(r'date(\srow10)?'))
        # source = soup.find_all()
        # time = soup.select('div.date, div.date.row10')
    print("Đã cào xong")
    print('Tiến hành xác định chuỗi')
    str=""
    for i in range(len(title)):
        str+=title[i].text + "\n"
        str+="- " + summary[i].text + "\n"   
        str+="- " + time[i].text + "\n"        
    return str

hyperLink = getLink(url)
hyperPostContent = getPostContent(hyperLink)

file_name = "cau3.txt"
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(hyperPostContent)
        

# print(hyperPostContent)