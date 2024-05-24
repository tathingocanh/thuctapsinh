''' TEXT FILE
Được cấu trúc như 1 dãy các dòng, mỗi dòng bao gồm một dãy các kí tự và một dòng tối thiểu là một kí tự dù cho dòng đó là dòng trống.
Các dòng trong text file được ngăn cách bởi một kí tự newline và mặc định trong Python chính là kí tự escape sequence newline \n.
'''
file = open('thuctapsinh')
print ( file)
doc = file.read()
file.close()
file = open('thuctapsinh')
doc2 = file.read(20)
file.close()
print(doc)
print(doc2)
file1 = open('thuctapsinh')
docdong = list(file1) # giống readlines
file1.close()
print(docdong)
'''file2 = open('thuctapsinh', mode= 'a+')
#file2.close()
viet= file2.write('\nta thi ngoc anh')
print(viet)
file2.close()'''
file3 = open('thuctapsinh')
doc3= file3.read()
file3.seek(10)
doc4= file3.read()
print(doc3)
print(doc4)
file3.close()
with open('thuctapsinh') as job: # tự đóng file
	data=job.read()
print(data)