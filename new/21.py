# thêm thư viên requests vào chương trình
# thư viên request chứa các phương thức với url
import requests
url = 'https://vnexpress.net/arsenal-sap-dung-tuong-wenger-4554241.html'
# request như một đối tượng, chưa nhiều phương thức
r = requests.get(url)
# print(r)
# phương thức get trả về một đối tượng res, chấm vào text để lấy thuộc tính text
print(r.text)