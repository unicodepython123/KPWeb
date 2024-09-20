import requests
from bs4 import BeautifulSoup
url="https://phongtro123.com/tinh-thanh/da-nang"
html = requests.get(url).text
#Tối ưu hóa code HTML bằng thư viện html5lib
# Muốn sử dụng các phương thức của đối tượng soup phải xử lý đối tượng trước như code dưới
soup = BeautifulSoup(html, 'html5lib')
# Sử dụng thư viện BeautifulSoup để bóc tách dữ liệu
# đầu vào là tag name và class hoặc những gì dùng để định danh thẻ đó
# thường sẽ là class vì lấy nhiều dữ liệu
TieuDe = soup.find_all("h3",class_="post-title")
# giá trị trả về là một đối tượng không phải text nên cần phải chấm vào thuộc tính text
DonGia = soup.find_all("span",class_="post-price") # lấy text của thẻ
DienTich = soup.find_all("span",class_="post-acreage")
DiaChi = soup.find_all("span",class_="post-location")
NgayDang = soup.find_all("time",class_="post-time")
str=""
for i in range(len(TieuDe)):
    # giá trị cần chấm text
    str+=TieuDe[i].text + "\n"
    str+="- " + DonGia[i].text + "\n"
    str+="- " + DienTich[i].text + "\n"
    str+="- " + DiaChi[i].text + "\n"
    str+="- " + NgayDang[i].text + "\n"
print(str)
35