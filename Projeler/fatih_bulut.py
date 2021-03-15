import random

sayi1=random.randint(1,100)
sayi2=random.randint(1,100)
islemler=["+", "-", "*", "/"]
islem=random.choice(islemler)

sonuctoplama = sayi1+sayi2
sonuccikarma = sayi1-sayi2
sonuccarpma = sayi1*sayi2
sonucbölme = sayi1/sayi2


if islem=="+":
    cevap=int(input("{}{}{}=? işleminin sonucu kaçtır?".format(sayi1,islem,sayi2)))
    if cevap==sonuctoplama:
      print("Tebrikler, bildin!")
    else:
      print("Bilemedin")
elif islem=="-":
    cevap=int(input("{}{}{}=? işleminin sonucu kaçtır?".format(sayi1,islem,sayi2)))
    if cevap==sonuccikarma:
      print("Tebrikler, bildin!")
    else:
      print("Bilemedin")
elif islem=="*":
    cevap=int(input("{}{}{}=? işleminin sonucu kaçtır?".format(sayi1,islem,sayi2)))
    if cevap==sonuccarpma:
      print("Tebrikler, bildin!")
    else:
      print("Bilemedin")
else:
    cevapbölme=input("{}{}{}=? işleminin sonucu kaçtır?".format(sayi1,islem,sayi2))
    print(cevapbölme)
    if cevapbölme==sonucbölme:
      print("Tebrikler, bildin!")
    else:
      print("Bilemedin")