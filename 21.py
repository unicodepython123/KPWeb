# Hỗ trợ gửi req đơn giản đến một url và xử lý phản hồi
import requests
url = 'https://vnexpress.net/thong-xe-duong-ten-lua-xoa-nut-co-chai-phia-tay-tp-hcm-4788879.html'
# Yêu cầu được gửi là Get (get được xem như 1 phương thức của request nhận đầu vào là 1 url)
r = requests.get(url)
print(r.text)
