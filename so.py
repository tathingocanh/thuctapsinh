print("helo")
a = 3
b=4
c=a+b
print(c)
d= 'hello'
print(d)
print(type(d))

# goi thu vien decimal
from decimal import*

# lay toi da 30 chu so phan nguyen va phan thap phan Decimal
getcontext().prec = 30
f = 10 / 3
print(f)
print(type(f))
 
e= Decimal(10)/Decimal(3)
print(e)


# so thap phan
from fractions import*
frac = Fraction(6,9)
print(frac)
print(type(frac))
print(frac+1)


#so phuc 
c= complex(2,5)
print(c)
print(c.real)
print(c.imag)


# toan tu
A=3
B=5
print(A/B)
print(A//B)
print(A%B)
print(A**B)


# thu vien math
import math
math.trunc(2.5)
print(math.trunc(2.5))
print(math.floor(2.5))
print(math.ceil(2.5))
print(math.fabs(-2.5))
print(math.sqrt(2.5))
print(math.gcd(2,5))