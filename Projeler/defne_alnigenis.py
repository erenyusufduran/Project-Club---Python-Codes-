#BEYKENT UNİVERSİTESİ TEMEL SEVİYE PHYTON PROJESİ
	#DEFNE ALNIGENİŞ 

#kolay seviye: TOPLAMA ve ÇIKARMA sayı aralıkları küçük
#orta seviye: DÖRT İŞLEM 1-99 aralığından seçim yapar
#zor seviye: DÖRT İŞLEM 100-300 aralığından seçim yapar

print("EN ÇOK KAÇ TANE BİLEBİLİRSİN?")
from random import randint
from random import choice
print('==========================')
liste=['+', '*', '-', '/']
liste2=['+', '-']
n=1
a=0

print("1. Kolay")
print("2. Orta")
print("3. Zor")
seviye=int(input("Oynamak istediğiniz seviyeyi seçiniz:"))
print(" ")

if seviye>3:
  seviye=int(input("Geçerli bir seviye giriniz: "))
  
if seviye==2 or seviye==3:
    print("İpucu: Bölme işlemi için virgülden sonra en fazla 2 basamak yaz :)")
    print(" ")
    print("==========================")

while n>0:
  if seviye==1: 
    sayi1=randint(1,30)
    sayi2=randint(1,sayi1)
    islem=choice(liste2)
  elif seviye==2:
    sayi1=randint(1,99)
    sayi2=randint(1,sayi1)
    islem=choice(liste)
  else:
    sayi1=randint(100,300)
    sayi2=randint(100,sayi1)
    islem=choice(liste)
  

  if islem=='+':
    sonuc= sayi1 + sayi2
  elif islem=='*':
    sonuc= sayi1 * sayi2
  elif islem=='/':
    sonucc=float(sayi1/sayi2)
    d=str(sonucc)
    e=d[0:4]
    sonuc=float(e)
  else:
    sonuc= sayi1 - sayi2
  
  cevap=float(input("{}{}{} işleminin sonucu nedir?".format(sayi1, islem, sayi2)))


  if cevap==sonuc:
    a=a+1
    print("Bravo, bildin!")
    print("==========================")
  else:
    n=0
    print("Bilemedin")
    print(" ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Doğru cevap sayısı: {}".format(a))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(" ")
    soru=str(input("Tekrar oynamak ister misin? [e]vet // [h]ayır"))
    print(" ")
    
    if soru== "e":
      a=0
      n=1
    else:
      print("Görüşmek Üzere!")
      print("==========================")
      
  if a==40:
    n=0
    print("Maksimum puana ulaştın, Tebrikler!")
    print("Doğru cevap sayısı: {}".format(a))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
