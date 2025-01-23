import numpy as np

print("1-D")

a=np.array([1,2,3,4]) #numpy dizisi oluşturur
print(a)

print(a.ndim) # oluşturulan dizinin kaç boyutlu olduğunu gösterir (number of dimension)
print(a.shape) # dizinin her boyuttaki eleman sayısını tuple olarak döndürür
print(len(a)) # first deminsion(satır sayısı row)

print("\n2-D")

b=np.array([[0,1,2],[3,4,5]]) # 2 * 3
print(b)

print(b.ndim) # 2 boyutu
print(b.shape) # (2,3)
print(len(b)) # 2