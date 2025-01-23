import numpy as np

a=np.random.randint(1,21,15) # 1'den 21'e kadat 15 tane random int array
# print(a)
# print(a%3==0)

b=np.array([1,2,3,4])
# print(b+1)
# print(b**2)

c=np.ones(4)+1
# print(c)

d=np.ones((3,3))
print(d)
print(d*d) # bu array çarpması değildir index bazında çarpar

print(d.dot(d)) # array çarpması budur