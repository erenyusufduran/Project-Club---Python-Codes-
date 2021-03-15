##Ödev
## Ferdi Özcan

import random as r
puan=0
while(True):
    print("Zorluk Seviyesini Seçiniz... \n 1. Seviye \n 2. Seviye \n 3. Seviye")
    print("çıkmak için -1")
    secim=int(input())
    bitis=10
    if (secim==1):
        bitis=100
    elif (secim==2):
        bitis=1000
    elif(secim==3):
        bitis=10000
    elif (secim==-1):
        break
    else:
        print("hatalı seçim")


    islemler=['+','-','*','/']

    islem=r.choice(islemler)
    sayi1=r.randint(0,bitis)
    sayi2=r.randint(0,bitis)
    sonuc=0
    if(islem=='+'):
        sonuc=sayi1+sayi2
    elif(islem=='-'):
        sonuc=sayi1-sayi2
    elif(islem=='/'):
        sonuc=sayi1/sayi2
    else:
        sonuc=sayi1*sayi2

    print(sayi1," ",islem," ",sayi2," = ?")
    kullanici=int(input("Sonucu Yazınız ----->"))
    if (sonuc==kullanici):
        print("Tebrikler Bildiniz!")
        puan=puan+5
    else:
        print("Hatalı Cevap")
        puan=puan-1

    print("Puanınız: ",puan)
    if(puan==100):
        print("Mükemmel! Oyunu Tamamladınız!")
        break

