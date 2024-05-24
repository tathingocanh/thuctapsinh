print('ta','ngoc','anh',sep='----')
print('ta','ngoc','anh',end='')
print('hi')

from time import sleep
print('start...')
sleep(3)  # dung chuong trinh 3s
print('end') 

print('start...',end='')
sleep(3)  # dung chuong trinh 3s
print('end..')
print()

from time import sleep

your_name = ""
your_great = "Hello! Xin chào các bạn nhé. Lại là bảnh đây."

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()
