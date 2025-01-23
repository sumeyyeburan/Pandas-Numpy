import numpy as np

a=np.array([1,2,3,4,5,6])
# print(a[-1])
# print(a[5:1:-1])
# print(a[0::2])

# a[3:]=10
# print(a)

b=a # referansı gönderildi
# print(b)
print(np.may_share_memory(a,b)) # bellekte aynı kısmı mı paylaşır

# a[4:]=5
# print(b) # a'daki değişiklik b'yi de etkiler

c=a.copy() # kopyası alınır
print(c)

a[4:]=5 # kopyası alındığı için a'daki değişiklik b'yi etkilemez
print(c)
print(np.may_share_memory(a,c))

