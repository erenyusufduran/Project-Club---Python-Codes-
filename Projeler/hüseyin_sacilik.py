print("Beykent Üniversitesi - Bilgisayarın rastgele ürettiği iki sayı ve işlemin sonucunu kullanıcıya soran uygulama projesi")
import math
import time
import random
seviye=0
print("Seviyeniz 0")
print( "0 altında ---> Troll","1-10--> İlkokul Terk", "10-15 Çok Tembel", "15-30 Tembel", "30-35 Normal", "35-40 Orta Şeker", "40-45 İyi", "45-60 Zeki Ama Çalışmıyor", "60-70 Akıllı", "70-90 Akıllı Bıdık", "90-120 Zeka Küpü", "120-150 Super Zeka", "150-170 Ultra Super Zeka", "170-230 Yok artık LeBron James", "360+ Einstein" )
islem=random.randint(1,4)
try:
    while True:
        if(islem==1):
            print("Sorunuz Geliyor...")
            time.sleep(3)
            print("Toplama İşlemi:)")
            sayi1= random.randint(1,600)
            sayi2= random.randint(1,600)
            print("Soru ----->",sayi1,"+",sayi2,"?")
            sonuc=int(input("Cevap:"))
            if(sayi1+sayi2==sonuc):
                    print("Tebrikler Doğru Cevap Seviyeniz +1 Değer Kazandı")
                    seviye= seviye +1
                    print("Seviyeniz",seviye)

            else:
                print("Cevabınız Yanlış Seviyeniz -1 Değer Kaybetti")
                seviye= seviye -1
                print("Seviyeniz ---->",seviye,)

        elif islem==2:
            print("Sorunuz Geliyor...")
            time.sleep(3)
            print("Çıkarma İşlemi:")
            sayı1=random.randint(1,600)
            sayı2=random.randint(1,600)
            print("Soru----->",sayı1,"-",sayı2,"?")
            sonuc=int(input("Cevap:"))
            if(sonuc==sayı1-sayı2):
                print("Cevabınız Doğru Seviyeniz +1 Değer Kazandı")
                seviye= seviye +1
                print("Seviyeniz",seviye,)

            else:
                print("Cevabınız Yanlış Seviyeniz -1 Değer Kaybetti")
                seviye= seviye -1
                print("Seviyeniz---->",seviye,)
        elif islem==3:
            print("Sorunuz Geliyor...")
            time.sleep(3)
            print("Çarpma İşlemi ---->")
            sayı1=random.randint(1,600)
            sayı2=random.randint(1,600)
            print("Soru --->",sayı1,".",sayı2,"?")
            sonuc=int(input("Cevap:"))
            if(sonuc==sayı1*sayı2):
                print("Cevabınız Doğru Seviyeniz +1 Değer Kazandı")
                seviye=seviye+1
                print("Seviyeniz----->",seviye,)

            else:
                print("Cevabınız Yanlış Seviyeniz -1 Değer Kaybetti")
                seviye=seviye-1
        elif islem==4:
            print("Sorunuz Geliyor...")
            time.sleep(3)
            print("Bölme İşlemi ---->")
            sayı1=random.randint(1,600)
            sayı2=random.randint(1,600)
            print("Soru--->",sayı1,":",sayı2,"?")
            sonuc=float(input("Cevap:"))
            if(sonuc==sayı1/sayı2):
                print("Cevabınız Doğru")
                seviye=seviye+1
                print("Seviyeniz---->",seviye,)

        else:
            print("Cevabınız Yanlış Seviyeniz -1 Değer Kaybetti ")
            seviye=seviye-1
            print("Seviyeniz---->",seviye,)

except:
    print("Bir hata ile karşılaşıldı. Uygulama kapatılıyor!")