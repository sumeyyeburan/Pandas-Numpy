import pandas as pd

titles=pd.read_csv('titles.csv')
cast=pd.read_csv('cast.csv')

print(cast.value_counts("character").head(10))
print("\n")
# character sütunundaki değerlere göre gruplar,aynı karakter adına sahip olan satırları bir araya toplar.
# n sütunundaki değerlerin toplamını alır,
print(cast.groupby("character")["n"].sum().sort_values(ascending=False).head(10))

# year sütununda hangi yılların kaç defa geçtiğini sayar,series olarak döner ve varsayılan büyükten küçüğe
# print(titles.value_counts("year").head(10))
# print("\n")
# year sütununa göre gruplar,title sütunundaki elemanların sayısını hesaplar, ascending=false olduğu için büyükten küçüğe sıralar
# print(titles.groupby("year")["title"].size().sort_values(ascending=False).head(10))