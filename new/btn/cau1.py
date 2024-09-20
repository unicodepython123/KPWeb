import os

url = 'https://baodaklak.vn/khoa-hoc-cong-nghe/'
hyperlink = [url]
for i in range (2,168):
    link = 'https://baodaklak.vn/khoa-hoc-cong-nghe/?paged='+str(i)
    hyperlink = hyperlink + [link]
print(hyperlink)

file_name = "cau1.txt"
with open(file_name, 'w', encoding='utf-8') as file:
    for link in hyperlink:
        file.write(link + '\n')

print(f"Đã ghi danh sách liên kết vào file {file_name}")
