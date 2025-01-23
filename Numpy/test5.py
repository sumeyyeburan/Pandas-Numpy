import numpy as np

a=np.array([1,2,3,4])
b=np.array([5,2,3,4])
c=np.array([1,2,3,4])

print(a==b) #index bazında bakar
print(np.array_equal(a,b)) # array bazında bakar