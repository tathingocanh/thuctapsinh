itera= [ i for i in range (3)]  # kieu tuple
print( itera)
itera= (i for i in range (3))  # mot iterator object
print( itera)
print(next(itera)) # tuy xuat tung gia tri
print(next(itera))
print(next(itera))

#ham tinh tong
tong=( i for i in range (10))
print(sum(tong))

# ham tim GTLN
ma = [1,3,4,2]
print(max(ma))
print(max([],default='max rong'))

# ham MIN tuong tu MAX

# ham sap xep
print(sorted(ma))
print(sorted(ma, reverse=True))