def anh():
	pass
	print('ngocanh')
anh()

def a():
	b=10
	c=20
	d=c + b 
	print(d)
a()
def b(a,b):
	print (a)
	print (b)
b('anh','18 tui')

def f(kteam=[]):
	kteam.append('f')
	print(kteam)
f()
f()
f()

def kteam(k,t,e,r):
	print(k)
	print(t,e)
	print('end',r)
lst = ['ta','thi','ngoc','anh']
kteam(*lst)

def anh(*args):
	print(args)
anh(*(3,5,6,7,8,1))

def a(name,member):
	print(name)
	print(member)
dic= {'name':'anh', 'member':18}
a(**dic)

def b(**a):
	for key, value in a.items():
		print(key,'=>', value)
b(ten='anh',tuoi=18)


def make_slogan():
	global kteam
	kteam = 'Howkteam'
make_slogan()
print(kteam)

def make_global():
	global x
	x=1
def local():
	x=5
	print('x=',x)
make_global()
print(x)
local()
print(x)

def cal_rec_per(width,height):
	per=(width+height)*2
	return per 
rec_1_width=5
rec_1_height=3
rec_1_per=cal_rec_per(rec_1_width,rec_1_height)
print(rec_1_per)
print(cal_rec_per(7,4))

def gen():
	while True:
		x=yield
		yield x**2
g=gen()
print(next(g))
print(g.send(2))
print(next(g))
print(g.send(10))


#lambda
ave= lambda a,b,c: (a+b+c)/3
print(ave(1,2,3))
a=[lambda x:x**2,lambda x: x**3]
print(a[1](2))
for i in a:
	print(i(3))

a=[1,2,3,4]
print(list(map(lambda x:x+1,a)))

tong=lambda x,y:x+y
a=[1,2,3,4]
b=[5,6,7,8]
c=(map(tong,a,b))
print(list(c))