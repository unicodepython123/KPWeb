import requests  # Nhập thư viện requests để gửi yêu cầu HTTP
import re  # Nhập thư viện re để làm việc với biểu thức chính quy
import os  # Nhập thư viện os để quản lý hệ thống tệp
from bs4 import BeautifulSoup  # Nhập BeautifulSoup từ thư viện bs4 để phân tích cú pháp HTML
from urllib.parse import urljoin, urlsplit  # Nhập các hàm để phân tích cú pháp và kết hợp URL

# Danh sách lưu trữ các liên kết đã được truy cập
links_seen = []
# Danh sách các liên kết cần truy cập, bắt đầu với trang chính của VnExpress
links_todo = ["https://vnexpress.net/"]

# Trích xuất tên miền từ liên kết đầu tiên trong danh sách
domain = urlsplit(links_todo[0]).netloc
# Đường dẫn đến thư mục nơi các tệp HTML sẽ được lưu
file_store = "E:/Files_Crawl/"

# Hàm chuyển đổi URL thành tên tệp hợp lệ
def url_to_file_name(url):
    # Chuyển đổi URL thành chuỗi, loại bỏ khoảng trắng và thay thế bằng dấu gạch dưới
    url = str(url).strip().replace(' ', '_')
    # Loại bỏ tất cả ký tự không hợp lệ, chỉ giữ lại chữ cái, số, dấu gạch ngang, dấu gạch dưới và dấu chấm
    return re.sub(r'(?u)[^-\w.]', '', url) + ".html"  # Trả về tên tệp với phần mở rộng .html

# Hàm tải và lưu nội dung của một URL vào tệp
def download(url):
    print("Saving file,...")  # In thông báo đang lưu tệp
    # Tạo đường dẫn tệp bằng cách kết hợp thư mục lưu và tên tệp từ URL
    filename = os.path.join(file_store, url_to_file_name(url))    
    # Mở tệp để ghi với mã hóa UTF-8
    with open(filename, 'w', encoding='utf-8') as the_html:
        # Ghi nội dung HTML của trang vào tệp
        the_html.write(requests.get(url).text)

# Hàm để truy cập một URL và xử lý các liên kết trong trang
def visit(url):
    global links_todo  # Khai báo sử dụng biến toàn cục links_todo

    links_seen.append(url)  # Thêm URL hiện tại vào danh sách các liên kết đã truy cập
    print("** Now visiting:", url)  # In thông báo đang truy cập URL

    # Gửi yêu cầu GET và lấy nội dung HTML của trang
    html = requests.get(url).text
    # Phân tích cú pháp nội dung HTML bằng BeautifulSoup
    html_soup = BeautifulSoup(html, "html5lib")
    download(url)  # Gọi hàm download để lưu nội dung trang

    Count = 0  # Biến đếm số liên kết mới tìm thấy
    # Tìm tất cả các thẻ <a> trong trang
    for link in html_soup.find_all("a"):
        link_url = link.get("href")  # Lấy thuộc tính href của thẻ <a>
        if link_url is None:  # Bỏ qua nếu không có giá trị href
            continue
        
        # Kết hợp URL tương đối với URL gốc để tạo thành URL đầy đủ
        full_url = urljoin(url, link_url)
        
        # Kiểm tra nếu tên miền của liên kết không khớp với tên miền gốc
        if urlsplit(full_url).netloc != domain:
            continue

        # Bỏ qua nếu URL có truy vấn (query string)
        if urlsplit(full_url).query != "":
            continue
        
        # Bỏ qua nếu liên kết đã có trong danh sách cần làm hoặc đã truy cập
        if full_url in links_todo or full_url in links_seen:
            continue
        
        Count += 1  # Tăng biến đếm khi tìm thấy một liên kết mới
        links_todo.append(full_url)  # Thêm liên kết mới vào danh sách cần truy cập

    # In thông báo số liên kết mới tìm thấy và số liên kết đã truy cập
    print(" + ", Count, "new link(s) found")
    print(" + ", len(links_seen), "link(s) seen/", len(links_todo), "link(s) need to do.")
    
    print("Enter to continue, ...")  # Thông báo yêu cầu nhấn Enter để tiếp tục
    input()  # Chờ người dùng nhấn Enter

# Vòng lặp chính để duyệt qua các liên kết cần truy cập
while links_todo:
    url_to_visit = links_todo.pop()  # Lấy liên kết cuối cùng trong danh sách
    visit(url_to_visit)  # Gọi hàm visit để xử lý liên kết đó
