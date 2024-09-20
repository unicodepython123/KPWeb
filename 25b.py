import requests
import re
import os

url="https://truyenfull.io/the-loai/kiem-hiep/"
html = requests.get(url).text


# Cách 2: Lấy link thông qua cấu trúc url
# Links_ToDo = [url]

# for i in range (2,38):
#     Link = "https://truyenfull.io/the-loai/kiem-hiep/trang-" + str(i) + '/'
#     Links_ToDo += [Link]
# print(Links_ToDo)


#Cách 1: Lấy link tự động từ Biểu thức chính quy - Sử dụng thuật toán đệ quy


def get_LinksbyRegEx(url_visit):
    global Links_ToDo
    print("** Now visiting:",url_visit)
    
    Links_seen.append(url_visit)    
    html = requests.get(url_visit).text
    NextLinks=re.findall('', html)

    for Link in NextLinks:
        if  Link not in Links_ToDo and Link not in Links_seen:
            Links_ToDo.append(Link)
        
    if Links_ToDo:
        get_LinksbyRegEx(Links_ToDo.pop())
    else:
        return

Links_ToDo=[url]
Links_seen=[]
get_LinksbyRegEx(Links_ToDo.pop())
print(len(Links_seen), "links found!")
    
