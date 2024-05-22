''' gioi han boi {}
cac phan tu cua dict phan cach boi dau ,
ccac phan tu cua dict phai la mot cap key-value
cap KEY-VALUE duoc phan cach boi dau :
cac key buoc phai la hash object'''

dic= { 1:'ta',2:'ngoc',3:'anh'}
print(dic)
print(type(dic))

dic0= { key: value for key, value in [(1,'ngoc'),(2,'anh')]}
print(dic0)

dic1 = dict()
print(dic1)

iter= ('name','number')
dic2 = dict.fromkeys(iter, 'anh')
print(dic2['name'])
dic2['name']= ' ngoc anh'
print(dic2)

dic3= dic.copy()
print(dic3)

dic3.clear()
print(dic3)

value=dic.get(1) # lay value theo key, khong co key thi value tra ve None
print(value)

value=dic.items()
print(value)

key= dic.keys() # lay ra danh sach key(values)
print(key)

pop = dic.pop(1) # bo di phan tu co key va tra ve value cua key do
print(pop)
print(dic)

popitem= dic.popitem() # tra ve 2-tuple voi key va value tuong ung
print(popitem)
print(dic)

value = dic0.setdefault(1)  # tra ve value cua key nhung k bo phan tu trong dict
print (value)
print(dic0)

d = {'a':1}
print(d)
update= d.update(b=2,c=3)
print(update)
print(d)