# A-Z về biểu thức chính quy
# ReGex là công cụ tìm từ hoặc nhóm từ có chung đặc điểm nào đó để tìm kiếm 
# Regex gồm 2 phần:
# Pattern và Flag --> /abc+c/g với abc+c là Pattern và g là flag
# Về flag
# g --> Tìm kiếm trong phạm vi toàn cục (tìm toàn bộ)
# i --> Cho phép tìm kiếm k phân biệt chữ hoa chữ thường
# m --> Tìm iếm trên nhiều dòng
# Nhóm kỳ hiệu 
# ^ --> Thể hiện vị trí đầu dòng --> /^a/ --> Tìm chữ a vị trí đầu dòng
# $ --> thể hiện vị trí cuối dòng --> /b$/ --> Tìm chữ b ở vị trí cuối dòng
# \b --> Thể hiện dấu cách --> / on/, /\bon/ --> Kết quả trả về là ' on', 'on'
# \d (0-9), \w (A-Z, a-z, 0-9,_), \s ( ), . --> Thể hiện một kiểu ký tự (0-9), (A-Z, a-z, 0-9,_), ( ) hoặc xuống dòng, bất kỳ ký tự gì không bao gồm xuống dòng
# Tập hợp ký tự và khoảng ký tự
# /[td]/ --> Tập hợp ký tự --> Tìm 1 ký tự nằm trong tập hợp ký tự
# [a-c] hoặc [0-9] --> Khoảng ký tự --> Tìm 1 ký tự nằm trong khoảng ký tự
# Nhóm ký tự định lượng
# {} --> Lặp đi lặp lại /3{3}/ --> Lặp lại số 3 3 lần --> kq: 3 số 3 liền kề
# {} --> Lặp đi lặp lại /3{3, }/ --> Lặp lại số 3 3 lần --> kq: ít nhất là 3 số 3 liền kề
# /\d+/ --> các số có theo sau là các số, lặp lại ít nhất 1 lần
# /\d0*/ --> Tìm một số, theo sau nó là một dãy các số 0 hoặc k có số 0 nào (* thể hiện có thể có lặp lại nhiều lần hoặc k có lặp lại nào)
# ? --> ký tự đặt trước nó có thể có hoặc k --> /u?abc/ --> kq: uabc hoặc abc
# group
# /(gogogo)*/ --> Nhóm các ký tự để xử lý --> gogogo lặp đi lặp lại của 3 chữ go 
# /(^gogogo)*/ --> Phủ định --> Không thuộc gogogo, tương tự như set goặc array
# (?<name>[0-9]{4}) --> Tên nhóm là name, bao gồm số từ 0 - 9, các số lặp đi lặp lại 4 lần (4 lần chọn số)
# | toán tử OR của ReGex

import re
import os
import requests

url = "https://phongtro123.com/tinh-thanh/da-nang/quan-ngu-hanh-son/phuong-my-an"
# lấy dữ liệu là html, html được hiểu là text
html= requests.get(url).text

# hàm findall nhận tham số là chuỗi cần tìm và chuổi tìm
# trả về có thể là string hoặc array
TieuDe = re.findall('<h3 class="post-title"><a.*?">(.*?)</a></h3>', html)
DonGia = re.findall('<span class="post-price">(.*?)</span>', html)
DienTich=re.findall('<span class="post-acreage">(.*?)</span>', html)
DiaChi= re.findall('<span class="post-location"><a.*?">(.*?)</a></span>', html)
NgayDang= re.findall('<time class="post-time" title=.*?">(.*?)</time>', html)
print(TieuDe)
# print(DonGia)
# print(DiaChi)

# Tạo đường dẫn phù hợp
# os.getcwd --> Lấy địa chỉ hiện tại của file đang chạy --> Lấy đó làm path để định nghĩa path mình muốn
# hàm join dùng để join đường dẫn hiện tại (chỉ lấy tới file trước file này) + đoạn text đường dẫn
# hàm path dựa trên đó mà tạo đường dẫn phù hợp với all hệ điều hành
file_path = os.path.join(os.getcwd(), "phongtro_data.txt")

# mở path, với chế độ w (ghi nếu đã tồn tại, tạo nếu chưa tồn tại), encoding="utf-8" để hiểu tiếng việt như 1 file
# tạo file
# trong file thực hiện write (ghi dữ liệu)
with open(file_path, "w", encoding="utf-8") as file:
    for i in range(len(TieuDe)):
        file.write(f"{TieuDe[i]}\n")
        file.write(f"- {DonGia[i]}\n")
        file.write(f"- {DienTich[i]}\n")
        file.write(f"- {DiaChi[i]}\n")
        file.write(f"- {NgayDang[i]}\n\n")

print(f"Dữ liệu đã được ghi vào file {file_path}")