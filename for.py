'''length =3 
iter_= (x for x in range (length))
c=0
while c< length:
	#print(next(iter_))
	#c+=1
	try :
		print(next(iter_))
	except StopIteration :
		break'''

iter_= (x for x in range (3))
for value in iter_ :
	print(value)

ten= {'ta':'thi','ngoc':'anh'}
for a,b in ten.items():
	print(a,b)

set_={5,8,1,9,4}
tong=0
for a in set_:
	tong+=a
print(tong)

print(list(range(3,6,2)))
lst = ['s',(1,2,3),{'abc','xyz'}]
for i in range(len(lst)):
	print(lst[i])

a = [1,3,4]
for i in range(len(a)):
	a[i]+=1
print(a)

anh= ['--'.join((a.capitalize(),b.upper()+c.lower())) for a,b,c in[ ('ta','thi','NGOC'),('dai','hoc','DDL')]]
print(anh)

hi= { key:value +1 for key,value in (('anh',18),('lan',21)) if value %2!=0}
print(hi)

enum=['anh','lan','thao','thuy']
gen= enumerate(enum,1)
print(list(gen))