import numpy as np #Numpy bir matematik kütüphanesi
import pandas as pd #Pandas düzgün veri çekebilmek için kullanılan kütüphane
import matplotlib.pyplot as plt #Matplotlib ise çizim yapabilmemiz için
from sklearn.preprocessing import PolynomialFeatures as pf
from sklearn.linear_model import LinearRegression
from sklearn import linear_model

veri = pd.read_csv("2016dolaralis.csv") #Verilerimizi alıyoruz.

x = veri["Gun"].to_frame() #Gün sütununu x'e atıyoruz.
y = veri["Fiyat"].to_frame() #iFyat sütununu y'ye atıyoruz.

x = pd.DataFrame(x).values
y = pd.DataFrame(y).values


plt.scatter(x,y)

""""""
#Linear Regression
tahminlinear = LinearRegression()
tahminlinear.fit(x,y) #Verilerimi oturtuyorum.
tahminLin = tahminlinear.predict(x) #Güne göre tahmin yapacağız.O yüzden x'i aldık.
#Bu işlemler sonucunda tahmin ettirdik. Şimdi çizdirmeye geçelim.

plt.plot(x,tahminLin,color="red")


#Polynomial Regression
tahminpolinom = pf(degree=6) #6.dereceden bir polinom olacağını belirttik.Dereceleri değişterek hangisinde daha iyi sonuçlar aldığımızı görebiliriz.
xYeni = tahminpolinom.fit_transform(x) #Oturtulmuş x değerlerini yeni bir değişkene atadık.
#xYeni tahmin  yapabilmemiz için oluşturduğumuz bir araform.
polinomModel = LinearRegression()
polinomModel.fit(xYeni,y) #Şimdi tekrar linear olarak oluşturup,oturttuk.
tahminPol = polinomModel.predict(xYeni)

plt.plot(x,tahminPol,color="green")

#Linearin mi,polinomun mu daha iyi olduğunu anlamak için:

hataKaresiLinear = 0
hataKaresiPolinom = 0

for i in range(len(xYeni)):
    hataKaresiPolinom = hataKaresiPolinom + (float(y[i])-float(tahminPol[i]))**2 #(Gerçek-Tahminimiz)'in karesi
    #Tüm elemanlar için uzaklıkları toplayacak.

for i in range(len(y)):
    hataKaresiLinear = hataKaresiLinear + (float(y[i])-float(tahminLin[i]))**2


#Hata oranı küçük olan daha iyi anlamına geliyor.
print("Linear Hata : ",hataKaresiLinear)
print("Polinom Hata : ",hataKaresiPolinom)
print("\n")

#Hangi dereceden polinom en iyi sonucu verir ona bakalım:
derece = 0
for a in range(100): #100.dereceye kadar bakacak.
    tahminpolinom = pf(degree=a+1) #0'dan başlıyor.a+1 ile 1.dereceden itibaren bakacak.
    xYeni = tahminpolinom.fit_transform(x)  # Oturtulmuş x değerlerini yeni bir değişkene atadık.
    # xYeni tahmin  yapabilmemiz için oluşturduğumuz bir araform.
    polinomModel = LinearRegression()
    polinomModel.fit(xYeni, y)  # Şimdi tekrar linear olarak oluşturup,oturttuk.
    tahminPol = polinomModel.predict(xYeni)

    for i in range(len(xYeni)):
        derece = derece + (float(y[i]) - float(tahminPol[i])) ** 2  # (Gerçek-Tahminimiz)'in karesi
        # Tüm elemanlar için uzaklıkları toplayacak.
    print(a + 1, ". dereceden fonksiyonda hata : ", derece)
    derece = 0


plt.show()