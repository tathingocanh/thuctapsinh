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