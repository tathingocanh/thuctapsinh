import requests
from bs4 import BeautifulSoup
import psycopg2

# URL của trang web
url = 'https://masothue.com/3703233116-cong-ty-tnhh-an-moc-quan'

# Lấy dữ liệu từ URL
response = requests.get(url)
#soup = BeautifulSoup(response.text, 'html.parser')

# Tìm thông tin cần thiết
'''def extract_info(soup):
    # Thay đổi các selector để phù hợp với cấu trúc HTML của trang web
   # name = soup.find('th', colspan="2").text.strip()
    name = soup.find('th', colspan="2")
    name = name.text.strip() if name else 'Không tìm thấy mã số thuế'
    masothue = soup.find('td', itemprop='taxID').text.strip()
    sdt = soup.find('td', itemprop='telephone').text.strip()
    dc = soup.find('td', itemprop='address').text.strip()
    return name, masothue, sdt, dc

name, masothue, sdt, dc = extract_info(soup)
'''
if response.status_code == 200:
    # Phân tích HTML của trang web
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Tìm thông tin mã số thuế
    name = soup.find('th', colspan="2")
    name = name.text.strip() if name else 'Không tìm thấy mã số thuế'
    masothue = soup.find('td', itemprop='taxID')
    masothue = masothue.text.strip() if masothue else 'Không tìm thấy mã số thuế'
    
    # Tìm thông tin số điện thoại
    sdt = soup.find('td', itemprop='telephone')
    sdt = sdt.text.strip() if sdt else 'Không tìm thấy số điện thoại'
    dc = soup.find('td', itemprop='address')
    dc = dc.text.strip() if dc else 'Không tìm thấy số điện thoại'
    
    # In thông tin ra màn hình
    print(f'name: {name}')
    print(f'Mã số thuế: {masothue}')
    print(f'Số điện thoại: {sdt}')
    print(f'địa chỉ: {dc}')
else:
    print(f'Không thể truy cập trang web, mã lỗi: {response.status_code}')


# Kết nối đến cơ sở dữ liệu PostgreSQL
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='123456',
    host='localhost',  # Hoặc địa chỉ của server PostgreSQL của bạn
    port='5432'        # Cổng kết nối (mặc định là 5432)
)

# Tạo con trỏ để thực hiện các lệnh SQL
cur = conn.cursor()

# Tạo câu lệnh SQL để chèn dữ liệu vào bảng
insert_query = """
    INSERT INTO thongtindoanhnghiep (name, masothue, sdt, dc)
    VALUES (%s, %s, %s, %s)
"""

# Chèn dữ liệu vào bảng
cur.execute(insert_query, (name , masothue, sdt , dc ))

# Commit giao dịch
conn.commit()

# Đóng kết nối
cur.close()
conn.close()

print("Dữ liệu đã được lưu thành công!")
