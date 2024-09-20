import re
import requests
import os

url = 'https://philong.com.vn/may-tinh-xach-tay.html?filter=135'

# Gửi yêu cầu GET và lấy nội dung HTML
res = requests.get(url)
html = res.text

# # Biểu thức chính quy để lấy nội dung bên trong thẻ <a> trong thẻ <h4> với lớp p-name line-clamp-2
# # Nội dung cần lấy là những ngoặc đơn được cấu hình theo như Regex
# pattern_title = r'<h4 class="p-name line-clamp-2">\s*<a href=".*?" title=".*?">(.*?)</a>\s*</h4>'
# matches_title = re.findall(pattern_title, html)
# for i in range (0, len(matches_title)):
#     print(i)    
#     print(matches_title[i])

# # Biểu thức chusnh quy để lấy nội dung bên trong thẻ span
# pattern_price = r'<span class="p-price\s*">\s*(.*?)\s*</span>'
# matches_price = re.findall(pattern_price, html)
# for i in range (0, len(matches_price)):
#     print(i)    
#     print(matches_price[i])
    
# # Xử lý mô tả và thông tin khuyến mãi

# Hàm xử lý mô tả:
# def FindallSumary (text):    
#     concat = []
#     for i in text:
#         if 'span' in i:
#             # Hàm thay thế, nhận đầu vào là chuỗi cần thay thế, chuỗi thay thế và đoạn text ban đầu 
#             print('span vào đây')
#             needed = re.sub('<span.*?>|</span>','', i)
#         elif 'strong' in i:
#             print('strong vào đây')
#             needed = re.sub('<strong.*?>|</strong>','', i)
#         else: 
#             needed = i
#             return needed
#         concat.append(needed)
#     return ' '.join(concat)

# # Lấy nội dung trong div class p-summary
# # pattern_summary = r'<div class="p-summary">\s*<p>(.*?)</p>\s*<p>(.*?)</p>\s*<p>(.*?)</p>\s*<p>(.*?)</p>\s*<p>(.*?)</p>\s*<p>(.*?)</p>\s*</div>'
# pattern_summary = r'<div class="p-summary">\s*((<p>.*?</p>\s*)+)</div>'

# # kết quả nhận được là 1 array có các phần từ ở dạng tupe
# SumaryRaw = re.findall(pattern_summary,html)
# Sumary = [FindallSumary(text) for text in SumaryRaw] 
# for i in range (0, len(Sumary)):
#     print(i)
#     print(Sumary[i])  
    
# Hàm xử lý khuyến mãi:
def findAllPromotion (text):
    pattern = r'</?(ul|li|p|span|strong)(\s[^>]*)?>' # Xóa các thẻ HTML
    cleaned_content = re.sub(pattern, '', text, flags=re.IGNORECASE) # biến các pattern thành những thẻ
    
    pattern = r'<a\s+href="[^"]*"[^>]*>.*?</a>' # xoá thẻ a và nội dung trong thẻ
    cleaned_content = re.sub(pattern, '', cleaned_content, flags=re.DOTALL)
    
    return cleaned_content

pattern_promotion = r'<span class="p-promotion" title="">(.*?)</span></p></span>'
# re.DOTALL cho phép hiểu ký tự . là xuống dòng 
PromotionRaw = re.findall(pattern_promotion, html,re.DOTALL)

Promotion = [findAllPromotion(text) for text in PromotionRaw]
for i in range (0, len(PromotionRaw)):
    print(i)
    print(PromotionRaw[i])

# file_path = os.path.join(os.getcwd(), "philong_data.txt")

# with open(file_path, "w", encoding="utf-8") as file:
#     for i in range(len(matches_title)):
#         file.write(f"{matches_title[i]}\n")
#         file.write(f"- {matches_price[i]}\n")
#         file.write(f"- {Sumary[i]}\n")
#         file.write(f"- {Promotion[i]}\n")

# print(f"Dữ liệu đã được ghi vào file {file_path}")



    
    
    

