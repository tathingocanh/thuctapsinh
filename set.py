''' set nam trong dau {}
set khong chua nhieu hon 1 phan tu trung lap'''

set_1 = {3,6,4,6,2}
print(set_1)

# toan tu
print(1 in set_1)

set_2= {3,5,6,4,7}
print(set_1-set_2) # difference

print(set_1&set_2)  #intersection


print(set_1|set_2) # union


print(set_1^set_2) # symmetric_differrence

'''set_1.clear()
print(set_1)'''

set_1.pop()
print(set_1)

set_2.remove(3) # discard giong remove nhung khi xoa phan tu k co thi se khong bao loi
print(set_2)

set1={1,2,3}
set1.add((4,5))
print(set1)

set1.update('hello',(7,8))
print(set1)


