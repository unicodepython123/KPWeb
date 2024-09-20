import requests  # Nhập thư viện requests để gửi yêu cầu HTTP
import re  # Nhập thư viện re để làm việc với biểu thức chính quy
import os  # Nhập thư viện os để quản lý hệ thống tệp
from bs4 import BeautifulSoup  # Nhập BeautifulSoup từ thư viện bs4 để phân tích cú pháp HTML/XML
from urllib.parse import urlsplit  # Nhập hàm urlsplit để phân tích cú pháp URL

# Đường dẫn đến thư mục nơi các tệp sẽ được lưu
file_store = "D:/Files_Crawl/"

# Địa chỉ URL của feed RSS
url_fileRSS = "https://vnexpress.net/rss/the-thao.rss"
# Trích xuất tên miền từ URL feed RSS
domain = urlsplit(url_fileRSS).netloc

# Hàm chuyển đổi URL thành tên tệp hợp lệ
def url_to_file_name(url):
    # Chuyển đổi URL thành chuỗi, loại bỏ khoảng trắng và thay thế bằng dấu gạch dưới
    url = str(url).strip().replace(' ', '_')
    # Loại bỏ tất cả ký tự không hợp lệ, chỉ giữ lại chữ cái, số, dấu gạch ngang, dấu gạch dưới và dấu chấm
    return re.sub(r'(?u)[^-\w.]', '', url) + ".txt"  # Trả về tên tệp với phần mở rộng .txt

# Hàm lưu nội dung của URL vào tệp
def save_toTXT(url):
    print("Saving file,...")  # In thông báo đang lưu tệp
    
    # Gửi yêu cầu GET và lấy nội dung HTML của trang
    html = requests.get(url).text
    # Phân tích cú pháp nội dung HTML bằng BeautifulSoup
    soup = BeautifulSoup(html, "html5lib")
    
    try:
        # Tìm thẻ <h1> với class là "title-detail"
        Title = soup.find("h1", class_="title-detail")    
        # Tìm thẻ <p> với class là "description"
        Desc = soup.find("p", class_="description")    
        # Tìm thẻ <article> với class là "fck_detail"
        Detail = soup.find("article", class_="fck_detail")
        # Kết hợp nội dung từ các thẻ tìm được
        Content = Title.text + "\n" + Desc.text + "\n" + Detail.text
        
        # Tạo đường dẫn tệp bằng cách kết hợp thư mục lưu và tên tệp từ URL
        filename = os.path.join(file_store, url_to_file_name(url))    
        # Mở tệp để ghi với mã hóa UTF-8
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(Content)  # Ghi nội dung vào tệp
    finally:
        return  # Kết thúc hàm

# Hàm để truy cập một URL và lưu nội dung
def visit(url):
    print("** Now visiting:", url)  # In thông báo đang truy cập URL
    save_toTXT(url)  # Gọi hàm lưu nội dung vào tệp

# Hàm lấy các liên kết từ feed RSS
def getURL_from_fileRSS(url_fileRSS):
    # Gửi yêu cầu GET và lấy nội dung XML của feed RSS
    xml = requests.get(url_fileRSS).text
    # Sử dụng biểu thức chính quy để tìm tất cả các liên kết trong thẻ <a>
    links = re.findall('<a href="(.*?)"', xml)
    
    links_todo = []  # Danh sách chứa các liên kết hợp lệ
    for link_url in links:
        if link_url is None:  # Bỏ qua nếu liên kết là None
            continue      
        
        # Kiểm tra nếu tên miền của liên kết không khớp với tên miền của feed RSS
        if urlsplit(link_url).netloc != domain:
            continue
        
        # Kiểm tra nếu liên kết đã có trong danh sách
        if link_url in links_todo:
            continue
        
        # Thêm liên kết hợp lệ vào danh sách
        links_todo.append(link_url)

    return links_todo  # Trả về danh sách các liên kết hợp lệ

# Gọi hàm để lấy các liên kết từ feed RSS
links_todo = getURL_from_fileRSS(url_fileRSS)
# Trong khi còn liên kết để truy cập
while links_todo:
    # Lấy liên kết cuối cùng trong danh sách
    url_to_visit = links_todo.pop()
    visit(url_to_visit)  # Gọi hàm để truy cập liên kết đó
