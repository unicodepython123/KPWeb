# Thư viên re hỗ trợ tìm kiếm
import re
string = 'Lionel Messi was born on 24 June 1987 in Rosario, Santa Fe.In the 2022 FIFA World Cup final on 18 December, Messi made his record 26th World Cup finals appearance at Lusail Stadium'
# Biểu thức chính quy, đại diện/định dạng cho các chuỗi ký tự tùy vào cách viết
pattern = '\d+'
# tìm kiếm tất cả các pattern trong string, kết quả trả về là các chuỗi theo đúng định dạng của parttern
result = re.findall(pattern, string)
print(result)