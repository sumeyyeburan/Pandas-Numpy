import numpy as np

a=np.arange(10) # 0'dan 9'a kadar olan sayılardan bir array oluşturur(10 elemanlı)
# print(a)
print(a.dtype)

b=np.arange(1,10,2) # start,end,step
# print(b)

c=np.linspace(1,2,5) # 1 ile 2 arasında 5 tane noktalı dizi oluşturur(eşit aralıklı,1 ve 2 de dahil)
# print(c)
print(c.dtype)

d=np.linspace(1,2,5,endpoint=False) # start,end,num-points (end elemanı dahil olmayacak)
# print(d)

x=np.ones((3,3)) # 3 x 3 lük 1 matrisi oluşturur
# print(x)
print(x.dtype)

y=np.zeros((2,3)) # 2 x 3 lük 0 matrisi
# print(y)
print(y.dtype)

z=np.random.rand(15) # 0-1 arasında 5 elemanlı random array(pozitif sayılar)
# print(z)
print(z.dtype)

s=np.random.randn(5) # 0-1 arasında tüm tam sayılar(negatif de dahil)
# print(s) 

n=np.array([1,2,3],dtype=float)
print(n)
print(n.dtype)