import requests  # Nhập thư viện requests để gửi yêu cầu HTTP
import re  # Nhập thư viện re để làm việc với biểu thức chính quy
import os  # Nhập thư viện os để quản lý hệ thống tệp
from urllib.parse import urlsplit  # Nhập hàm urlsplit để phân tích cú pháp URL

# Đường dẫn đến thư mục nơi các tệp HTML sẽ được lưu
file_store = "D:/Files_Crawl/"
# Địa chỉ URL của feed RSS
url_fileRSS = "https://vtc.vn/rss/suc-khoe.rss"

# Trích xuất tên miền từ URL feed RSS
domain = urlsplit(url_fileRSS).netloc

# Hàm chuyển đổi URL thành tên tệp hợp lệ
def url_to_file_name(url):
    # Chuyển đổi URL thành chuỗi, loại bỏ khoảng trắng và thay thế bằng dấu gạch dưới
    url = str(url).strip().replace(' ', '_')
    # Loại bỏ tất cả ký tự không hợp lệ, chỉ giữ lại chữ cái, số, dấu gạch ngang, dấu gạch dưới và dấu chấm
    return re.sub(r'(?u)[^-\w.]', '', url) + ".html"  # Trả về tên tệp với phần mở rộng .html

# Hàm tải và lưu nội dung của một URL vào tệp
def download(url):
    print("Saving file,...")  # In thông báo đang lưu tệp
    # Gửi yêu cầu GET và lấy nội dung HTML của trang
    content = requests.get(url).text    
    # Tạo đường dẫn tệp bằng cách kết hợp thư mục lưu và tên tệp từ URL
    filename = os.path.join(file_store, url_to_file_name(url))    
    
    # Mở tệp để ghi với mã hóa UTF-8
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)  # Ghi nội dung vào tệp
    
# Hàm để truy cập một URL và lưu nội dung
def visit(url):
    print("** Now visiting:", url)  # In thông báo đang truy cập URL    
    download(url)  # Gọi hàm download để lưu nội dung trang

# Hàm lấy các liên kết từ feed RSS
def getURL_from_fileRSS(url_fileRSS):
    # Gửi yêu cầu GET và lấy nội dung XML của feed RSS
    xml = requests.get(url_fileRSS).text
    # Sử dụng biểu thức chính quy để tìm tất cả các thẻ <link>
    links = re.findall('<link>(.*?)</link>', xml)    
    
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

# Vòng lặp chính để duyệt qua các liên kết cần truy cập
while links_todo:
    url_to_visit = links_todo.pop()  # Lấy liên kết cuối cùng trong danh sách
    print(url_to_visit)  # In ra liên kết đang truy cập
    new_links = visit(url_to_visit)  # Gọi hàm visit để xử lý liên kết đó
