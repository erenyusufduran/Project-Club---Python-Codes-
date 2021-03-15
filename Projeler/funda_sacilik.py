print("Random Matematiksel İşlemler")
import math
import time
import random
rutbe=0
print("Rütbeniz 0 Acemi")
print( "0 dan az ---> Berbat", "1-10--> Acemi", "10-15 Normal", "15-30 Yetkin", "30+ Uzman" )
islem=random.randint(1,4)
while True:
    if(islem==1):
        print("Sorunuz Hazırlanıyor")
        time.sleep(3)
        print("İşleminiz Toplama:)")
        sayi1= random.randint(1,600)
        sayi2= random.randint(1,100)
        print("Soru ----->",sayi1,"+",sayi2,"?")
        sonuc=int(input("Cevap:"))
        if(sayi1+sayi2==sonuc):
            print("Cevabınız Doğru Rütbeniz +1 Değer Kazanmıştır")


            rutbe= rutbe +1
            print("Rütbeniz",rutbe)

        else:
            print("Cevabınız Yanlış Rütbeniz -1 Değer Kazanmıştır")
            rutbe= rutbe -1
            print("Rütbeniz ---->",rutbe,)

    elif islem==2:
        print("Sorunuz Hazırlanıyor")
        time.sleep(3)
        print("İşleminiz Çıkarma:")
        sayı1=random.randint(1,100)
        sayı2=random.randint(1,100)
        print("Soru----->",sayı1,"-",sayı2,"?")
        sonuc=int(input("Cevap:"))
        if(sonuc==sayı1-sayı2):
            print("Cevabınız Doğru Rütbeniz +1 Değer Kazanmıştır")
            rutbe= rutbe +1
            print("Rütbeniz",rutbe,)

        else:
            print("Cevabınız Yanlış Rütbeniz -1 Değer Kazanmıştır")
            rutbe= rutbe -1
            print("Rütbeniz---->",rutbe,)
    elif islem==3:
        print("Sorunuz Hazırlanıyor..")
        time.sleep(3)
        print("İşleminiz Çarpma ---->")
        sayı1=random.randint(1,100)
        sayı2=random.randint(1,100)
        print("Soru --->",sayı1,".",sayı2,"?")
        sonuc=int(input("Cevap:"))
        if(sonuc==sayı1*sayı2):
            print("Cevabınız Doğru Rütbeniz +1 Değer Kazanmıştır")
            rutbe=rutbe+1
            print("Rütbeniz----->",rutbe,)

        else:
            print("Cevabınız Yanlış Rütbeniz -1 Değer Kazanmıştır")
            rutbe=rutbe-1
    elif islem==4:
        print("Sorunuz Hazırlanıyor..")
        time.sleep(3)
        print("İşleminiz bölme ---->")
        sayı1=random.randint(1,100)
        sayı2=random.randint(1,100)
        print("Soru--->",sayı1,":",sayı2,"?")
        sonuc=float(input("Cevap:"))
        if(sonuc==sayı1/sayı2):
            print("Cevabınız Doğru")
            rutbe=rutbe+1
            print("Rütbeniz---->",rutbe,)

        else:
            print("Cevabınız Yanlış Rütbeniz -1 Değer Kazanmıştır ")
            rutbe=rutbe-1
            print("Rütbeniz---->",rutbe,)



