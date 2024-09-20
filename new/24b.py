# hỗ trợ hoàn thiện cấu trúc HTML, nếu HTML đưa vào bị thiếu
from bs4 import BeautifulSoup
# đoạn html cần tìm dữ liệu
broken_html = '<ul><li>Coffee<li>Tea</li><li>Milk</li></ul>'
# Trả về đối tượng html đã được bổ dung phần còn thiếu nhờ html5lib
soup = BeautifulSoup(broken_html, 'html5lib')
# chỉnh sửa bản soup thành bản đẹp, thông qua phương thức của soup
fixed_html = soup.prettify()
print(fixed_html)