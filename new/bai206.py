# tổng quan về bài tập:
# Ví dụ này sử dụng các yêu cầu và Beautiful Soup,
# cũng như thư viện tập dữ liệu, minh họa cách bạn có thể chạy lại trình thu thập dữ liệu
# mà không lưu trữ các kết quả trùng lặp.

import requests  # Nhập thư viện requests để gửi yêu cầu HTTP
import dataset  # Nhập thư viện dataset để làm việc với cơ sở dữ liệu SQLite
import re  # Nhập thư viện re để làm việc với biểu thức chính quy
from datetime import datetime  # Nhập lớp datetime để làm việc với thời gian
from bs4 import BeautifulSoup  # Nhập BeautifulSoup từ thư viện bs4 để phân tích cú pháp HTML
from urllib.parse import urljoin, urlparse  # Nhập các hàm để xử lý URL

# Kết nối đến cơ sở dữ liệu SQLite có tên 'books.db'
db = dataset.connect('sqlite:///books.db')
# Địa chỉ cơ sở của trang web để thu thập dữ liệu
base_url = 'http://books.toscrape.com/'

# Hàm thu thập dữ liệu sách từ HTML đã phân tích
def scrape_books(html_soup, url):
    # Duyệt qua từng sản phẩm sách trong HTML
    for book in html_soup.select('article.product_pod'):
        # Lấy URL của sách từ thẻ <h3>
        book_url = book.find('h3').find('a').get('href')
        # Tạo URL đầy đủ bằng cách kết hợp với URL gốc
        book_url = urljoin(url, book_url)
        # Phân tích URL để lấy đường dẫn
        path = urlparse(book_url).path
        # Lấy ID sách từ đường dẫn
        book_id = path.split('/')[2]
        # Thêm hoặc cập nhật thông tin sách vào cơ sở dữ liệu
        db['books'].upsert({'book_id': book_id, 'last_seen': datetime.now()}, ['book_id'])

# Hàm thu thập thông tin chi tiết của một cuốn sách
def scrape_book(html_soup, book_id):
    # Tìm phần chính của sách trong HTML
    main = html_soup.find(class_='product_main')
    book = {}  # Khởi tạo từ điển để lưu thông tin sách
    book['book_id'] = book_id  # Lưu ID sách
    # Lấy tiêu đề sách
    book['title'] = main.find('h1').get_text(strip=True)
    # Lấy giá sách
    book['price'] = main.find(class_='price_color').get_text(strip=True)
    # Lấy thông tin tồn kho
    book['stock'] = main.find(class_='availability').get_text(strip=True)
    # Lấy đánh giá sách
    book['rating'] = ' '.join(main.find(class_='star-rating').get('class')).replace('star-rating', '').strip()
    # Lấy đường dẫn hình ảnh của sách
    book['img'] = html_soup.find(class_='thumbnail').find('img').get('src')
    
    # Tìm mô tả sách
    desc = html_soup.find(id='product_description')
    book['description'] = ''  # Khởi tạo mô tả sách là chuỗi rỗng
    if desc:  # Nếu có mô tả
        book['description'] = desc.find_next_sibling('p').get_text(strip=True)
    
    # Tìm bảng thông tin sản phẩm
    info_table = html_soup.find(string='Product Information').find_next('table')
    # Duyệt qua từng hàng trong bảng thông tin
    for row in info_table.find_all('tr'):
        header = row.find('th').get_text(strip=True)  # Lấy tiêu đề của hàng
        # Làm sạch tiêu đề để phù hợp với tên cột trong SQLite
        header = re.sub('[^a-zA-Z]+', '_', header)
        value = row.find('td').get_text(strip=True)  # Lấy giá trị của hàng
        book[header] = value  # Lưu thông tin vào từ điển sách
    # Thêm hoặc cập nhật thông tin sách vào cơ sở dữ liệu
    db['book_info'].upsert(book, ['book_id'])

# Bắt đầu thu thập dữ liệu từ các trang trong danh mục
url = base_url  # Bắt đầu với URL cơ sở
inp = input('Do you wish to re-scrape the catalogue (y/n)? ')  # Hỏi người dùng có muốn thu thập lại không

# Vòng lặp để thu thập dữ liệu
while True and inp == 'y':
    print('Now scraping page:', url)  # In thông báo đang thu thập dữ liệu trang
    r = requests.get(url)  # Gửi yêu cầu GET đến URL
    html_soup = BeautifulSoup(r.text, 'html.parser')  # Phân tích cú pháp HTML
    scrape_books(html_soup, url)  # Gọi hàm để thu thập thông tin sách
    
    # Kiểm tra có trang tiếp theo không
    next_a = html_soup.select('li.next > a')
    if not next_a or not next_a[0].get('href'):  # Nếu không có trang tiếp theo
        break  # Kết thúc vòng lặp
    # Tạo URL cho trang tiếp theo
    url = urljoin(url, next_a[0].get('href'))

# Bây giờ thu thập từng cuốn sách theo thứ tự cũ nhất trước
books = db['books'].find(order_by=['last_seen'])  # Lấy danh sách sách đã thu thập, sắp xếp theo thời gian thấy lần cuối
for book in books:  # Duyệt qua từng cuốn sách
    book_id = book['book_id']  # Lấy ID sách
    book_url = base_url + 'catalogue/{}'.format(book_id)  # Tạo URL cho cuốn sách
    print('Now scraping book:', book_url)  # In thông báo đang thu thập dữ liệu cuốn sách
    r = requests.get(book_url)  # Gửi yêu cầu GET đến URL sách
    r.encoding = 'utf-8'  # Đặt mã hóa cho phản hồi
    html_soup = BeautifulSoup(r.text, 'html.parser')  # Phân tích cú pháp HTML
    scrape_book(html_soup, book_id)  # Gọi hàm để thu thập thông tin chi tiết cuốn sách
    # Cập nhật thời gian thấy lần cuối
    db['books'].upsert({'book_id': book_id, 'last_seen': datetime.now()}, ['book_id'])






