import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite mới hoặc tạo cơ sở dữ liệu nếu chưa tồn tại
conn = sqlite3.connect('books.db')

# Tạo một đối tượng cursor để thực thi các lệnh SQL
cursor = conn.cursor()

# Tạo bảng 'books'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id TEXT PRIMARY KEY,
        last_seen TIMESTAMP
    )
''')

# Tạo bảng 'book_info'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book_info (
        book_id TEXT PRIMARY KEY,
        title TEXT,
        price TEXT,
        stock TEXT,
        rating TEXT,
        img TEXT,
        description TEXT,
        upc TEXT,
        asin TEXT,
        publish_date TEXT,
        author TEXT,
        genre TEXT,
        availability TEXT
    )
''')

# Lưu các thay đổi và đóng kết nối
conn.commit()
conn.close()

print("Database and tables created successfully!")
