import requests  # Nhập thư viện requests để gửi yêu cầu HTTP và nhận phản hồi từ web.

from bs4 import BeautifulSoup  # Nhập lớp BeautifulSoup từ thư viện bs4 để phân tích cú pháp HTML dễ dàng.

# Đặt URL đến trang IMDb cụ thể chứa danh sách các tập của bộ phim có mã 'tt0944947'.
url = 'http://www.imdb.com/title/tt0944947/episodes/'

# Thêm User-Agent để mô phỏng trình duyệt
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Khởi tạo danh sách rỗng để lưu trữ số tập phim và đánh giá của chúng.
episodes = []  # Danh sách lưu số tập phim theo định dạng "mùa.tập".
ratings = []   # Danh sách lưu các đánh giá tương ứng với từng tập phim.

# Vòng lặp qua các mùa từ 1 đến 7. Số 7 có thể điều chỉnh tùy thuộc vào số mùa thực tế của bộ phim.
for season in range(1, 8):
    # Gửi yêu cầu GET đến URL với tham số mùa để truy xuất dữ liệu cho từng mùa cụ thể.
    r = requests.get(url, headers=headers, params={'season': season})
    # print(r.text)
    # Phân tích cú pháp nội dung HTML từ phản hồi, biến 'r.text' chứa mã HTML của trang.
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup)
    # Tìm phần chứa danh sách các tập phim trong trang HTML, xác định bằng class 'eplist'.
    # lấy được danh sách các div chưa thông tin tập phim
    listing = soup.find('section', class_='sc-e55007c4-0 fZcppP')
    # print(season)
    # print(listing)
    # print('')
    # Duyệt qua từng tập phim trong phần danh sách. 'enumerate' cung cấp chỉ số cho mỗi phần tử.
    # tìm được các div đầu tiên trong các div của listing
    # thực hiện đánh số cho tập phim
    # print(season)
    # print(listing)
    for epnr, article in enumerate(listing.find_all('article', recursive=False)):
        # Tạo số tập phim theo định dạng "mùa.tập", 'epnr + 1' để đánh số bắt đầu từ 1.
        episode = "{}.{}".format(season, epnr + 1)
        # Tìm phần tử chứa đánh giá của tập phim, xác định bằng class 'ipl-rating-star__rating'.
        # tìm được đánh giá thông qua div đầu tiên, find chỉ tìm cái đâuù tiên
        rating_el = article.find(class_='ipc-rating-star--rating')
        
        # Lấy giá trị đánh giá từ phần tử, loại bỏ khoảng trắng và chuyển đổi thành kiểu số thực.
        rating = float(rating_el.get_text(strip=True))
        # In số tập phim và đánh giá ra màn hình để người dùng thấy thông tin.
        print('Episode:', episode, '-- rating:', rating)
        
        # Thêm số tập phim và đánh giá vào các danh sách tương ứng để có thể sử dụng sau này.
        episodes.append(episode)  # Lưu số tập vào danh sách 'episodes'.
        ratings.append(rating)     # Lưu đánh giá vào danh sách 'ratings'.
        
import matplotlib.pyplot as plt
episodes = ['S' + e.split('.')[0] if int(e.split('.')[1]) == 1 else '' \
for e in episodes]
plt.figure()
positions = [a*2 for a in range(len(ratings))]
plt.bar(positions, ratings, align='center')
plt.xticks(positions, episodes)
plt.show()
        
