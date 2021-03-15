n = 0
puan = 0
print("Zorluk seviyesini seçiniz")
print("1. seviye")
print("2. seviye")
print("3. seviye")
zorluk=input("Zorluk seviyesini seçiniz:")
islem=(input("Pratik yapmak istediğiniz işlem seçiniz=+/-/*:"))
import random
while n<5:
    n=n+1
    if(zorluk=="1"):
        sayi1=random.randint(1,10)
        sayi2=random.randint(1,sayi1)
        sayi1>sayi2
    elif(zorluk=="2"):
        sayi1=random.randint(10,50)
        sayi2=random.randint(10,sayi1)
        sayi1>sayi2
    else:
        sayi1=random.randint(50,100)
        sayi2=random.randint(50,sayi1)
    if(islem=="+"):
        sonuc=sayi1+sayi2
    elif(islem=="-"):
        sonuc=sayi1-sayi2
    elif(islem=="*"):
        sonuc=sayi1*sayi2
    cevap=int(input("{}{}{}=? işleminin sonucunu bulunuz:".format(sayi1,islem,sayi2)))
    if cevap==sonuc:
        print("Tebrikler, bildin!")
        puan=puan+20
    else:
        print("Ups, yanlış oldu.")
        puan=puan-10
if(puan<=50):
    print("Puanın {}. Daha çok çalışmalısın.".format(puan))
elif(puan==70):
    print("Puanın {}.İyi gidiyorsun.".format(puan))
else:
    print("Puanın {}.Mükemmelsin.".format(puan))