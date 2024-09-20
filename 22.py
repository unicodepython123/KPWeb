# Bóc tách dữ liệu
# Có thể sử dụng biểu thức chính quy hoặc thư viên Beautiful Soup/html5lib để bóc tách dữ liệu

# RegEx là một chuỗi ký tự tạo thành một biểu mẫy tìm kiếm (search pattern)
# Dùng để kiểm tra xem một chuỗi có chứa mẫu tìm kiếm được chỉ định không
# ví dụ:
import re # cung cấp các công cụ để làm việc với biểu thức chính quy
string = 'Khoảng 300 m đường Tên Lửa, quận Bình Tân được mở rộng lên 40 m, 6 làn xe, nối thông ra tỉnh lộ 10 giúp xóa cảnh kẹt xe, ngập úng kéo dài nhiều năm. Đoạn nâng cấp dài 300 m, từ nút giao với đường số 29 đến tỉnh lộ 10, thông xe sáng 4/9 sau khoảng 5 tháng thi công. Khu vực này trước đây là các hẻm nhỏ, ngoằn ngoèo, được nâng cấp thành đường rộng 6 làn xe cùng hệ thống vỉa hè, thoát nước, chiếu sáng...'
# biểu thức chính quy để tìm các số (\d+)
pattern = '\d+' 
# hàm của re dùng để tìm tất cả các mẫy khớp với biểu thức
result = re.findall(pattern, string) 
print(result)
