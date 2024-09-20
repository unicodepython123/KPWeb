from bs4 import BeautifulSoup
import requests

# Định nghĩa headers để giả lập trình duyệt
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q=weather+{city}', headers=headers)
    print("Searching ...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)
    try:
        time = soup.select('#wob_dts')[0].getText().strip()
    except IndexError:
        time = "Không tìm thấy thông tin thời gian."

    try:
        info = soup.select('#wob_dc')[0].getText().strip()
    except IndexError:
        info = "Không tìm thấy thông tin trạng thái."

    try:
        weather = soup.select('#wob_tm')[0].getText().strip()
    except IndexError:
        weather = "Không tìm thấy thông tin nhiệt độ."

    print('Thời tiết:')
    print("Thời gian:", time)
    print("Trạng thái:", info)
    print("Nhiệt độ:", weather)

city = input("Enter the Name of Any City: ")
city = city + " weather"
weather(city)
