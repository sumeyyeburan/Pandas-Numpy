import numpy as np

a=np.array([[4,3,5],[1,2,1]])
b=np.sort(a,axis=1) # axis hangi eksenden yapılavağını söyler.axis=0 olsaydı column axis=1 olduğu için row.axis=1 default değerdir
print(b)

x=np.array([1.2,1.5,1.6,2.5,3.5,4.7])
print(np.around(x)) # en yakın çift sayıya yuvarlar(  .5 için) ve hala float olur
print(np.around(x).astype(int)) # int e çevrilir