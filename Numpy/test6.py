import numpy as np

a=np.array([1,2,3,1])
# print(np.sum(a))
# print(a.sum()) # sadece numpy kütüphanesi üzerinden oluşturulmuş listelerde kullanılır

# print(a.min())
# print(a.max())

# print(a.argmin()) #index dönürür
# print(a.argmax())

# print(np.all([True,False,True])) # and operatörü
# print(np.any([True,False,True])) # or operatörü

# b=np.zeros((5,5))
# print(np.any(b!=0)) # herhangi biri true
# print(np.all(b==b)) # hepsi true

print(a.mean()) # ortalaması
print(np.median(a)) # ortanca değer(büyükten küçüğe sıralayıp ortanda değeri bulur)
print(a.std()) #standart sapma