# thêm thư viên request để có thể get đucợ dữ liệu từ url
import requests
# thêm thư viện re để tìm kiếm dữ liệu
import re
# thêm thư viên os để ghi dữ liệu tìm được ra file
import os

url = 'https://phongtro123.com/tinh-thanh/da-nang/quan-thanh-khe/phuong-tam-thuan'
# phải chấm text để trả về dữ liệu
string = requests.get(url).text
pattern = '<h3 class="post-title">.*?> (.*?) </a></h3><div class="meta-row clearfix"><span class="post-price">(.*?)</span><span class="post-acreage">(.*?)</span><span class="post-location"><a .*?>(.*?)</a></span><time .*?>(.*?)</time>'
result = re.findall(pattern, string)
print(result)

# thư viện os cung cấp phương thức path để định nghĩa địa chỉ file
# os.getcwd là dùng để lấy địa chỉ hiện tại (chỉ lấy tới trước file đang sử dụng)
# dùng hàm join để nối địa chỉ hiện tại với tên file mới
# lệnh này giúp luôn tạo được 1 file đúng dù có gửi src đi bất kỳ đâu
file_path = os.path.join(os.getcwd(), "phongtro_data123.txt")

# mở path, với chế độ w (ghi nếu đã tồn tại, tạo nếu chưa tồn tại), encoding="utf-8" để hiểu tiếng việt như 1 file
# tạo file
# trong file thực hiện write (ghi dữ liệu)
with open(file_path, 'w', encoding="utf-8") as file:
    for i in range (0, len(result)):
        for j in range (0, len(result[i])):
            if (j >= 1):
                file.write(f'- {result[i][j]}\n')
            else:
                file.write(f'{result[i][j]}\n')