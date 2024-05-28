'''a=-2
b=1
if a==b:
	print("a bang b")
else :
	print("a khac b")
while a<0:
	print(a)
	a+=1
five_even_number=[]
k_number=1
while True:
	if k_number % 2==0:
		five_even_number.append(k_number)
		if len(five_even_number)==5:
			break
	k_number+=1
print(five_even_number)
print(k_number)

#k1= int(input('nhap so thu nhat:\n '))
#k2= int(input('nhap so thu 2:\n'))
#k3=int(input('nhapso thu 3:\n'))
#print(k1)
k1 = int(input('Nhap so thu nhat\n=> '))
k2 = int(input('Nhap so thu hai\n=> '))
k3 = int(input('Nhap so thu ba\n=> '))

if k1 > k2 and k1 > k3: print('so lon nhat la', k1)
elif k2 > k1 and k2 > k3: print('so lon nhat la', k2)
else: print('so lon nhat la', k3)'''

a= ('abcd sdfgyuy dfg Anh fgh werty fnm bnm Anh')
print(len(a))
