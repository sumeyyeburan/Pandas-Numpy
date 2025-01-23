import numpy as np

# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a.ravel()) # array'i birleştirir
# print(a.T) # kare matrix e çevirir
# print(a.T.ravel())

a=np.array([[1,2,3],[4,5,6]])
print(a.shape)

b=a.ravel()
print(b)

print(b.reshape(2,3)) # 2 x 3 lük matrix haline getirir
