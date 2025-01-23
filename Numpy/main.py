import pandas as p
import numpy as n
# # Series
# benimSozlugum={"Sumeyye":27,"Ayse":30,"Zeki":5}
# # print(p.Series(benimSozlugum)) #isimler index olur

# benimYaslarim=[10,20,30]
# benimIsimlerim=["Sumeyye","Ayse","Zeki"]

# # ilk parametre data,ikinci parametre liste olur
# # print(p.Series(data=benimYaslarim,index=benimIsimlerim))

# numpyDizisi=n.array([50,40,30])

# print(numpyDizisi)
# # print(p.Series(numpyDizisi))

data=n.random.randn(4,3)

dataFrame=p.DataFrame(data)
print(dataFrame[0])

