import random
import time
list = ["+","-","*","/"]
list2 = ["+","-"]
puan = 0
dogru = 0
yanlis = 0
print("## HOŞGELDİNİZ ##")
print("-"*30)
cevap = input("Oyun Kurallarını Öğrenmek İster Misiniz ? (e)vet , (h)ayır : ")
if cevap == "e":
    print(""" *** Oyun Kuralları ***
    1.Seviyede sadece toplama ve çıkarma işlemleri bulunmaktadır , deneme hakkınız : 6;
    her doğru cevabınız için 10 puan kazanacaksınız , her yanlış cevabınız için 2 puan kaybedeceksiniz

    2.Seviyede tüm işlemler bulunmaktadır, deneme hakkınız: 5
     her doğru cevabınız için 20 puan kazanacaksınız , her yanlış cevabınız için 4 puan kaybedeceksiniz

    3.Seviyede tüm işlemler bulunmakta ve sayılarımız en fazla 2 basamaklıdır, deneme hakkınız: 4
     her doğru cevabınız için 30 puan kazanacaksınız , her yanlış cevabınız için 6 puan kaybedeceksiniz

    4.Seviyede tüm işlemler bulunmakta ve sayılarımız en fazla 3 basamaklıdır, deneme hakkınız: 3
     her doğru cevabınız için 50 puan kazanacaksınız , her yanlış cevabınız için 10 puan kaybedeceksiniz""")
    print("-"*30)
    time.sleep(5)
print("""
    1.Seviye için {1}
    2.Seviye için {2}
    3.Seviye için {3}
    4.Seviye için {4}
    Oyundan çıkmak için {5}""")
while True:
    seviye = int(input(" Ne yapmak istersiniz ?"))
    if seviye == 1:
        islem = random.choice(list2)
        sayi1 = random.randint(0,9)
        sayi2 = random.randint(0,9)
        if islem == "+":
            sonuc = sayi1+sayi2
        else:
            sonuc = sayi1-sayi2
        for i in range (5, -1, -1):
            kullanici = int (input ("{} {} {} = ".format (sayi1,islem, sayi2)))
            if kullanici == sonuc:
                puan += 10
                print ("Tebrikler.. Puanınız : {}".format (puan))
                dogru +=1
                break
            elif i > 0:
                puan -= 2
                print ("Tekrar deneyiniz ,puanınız {} ve kalan hakkınız {}".format (puan, i))
                yanlis +=1
            else:
                print ("Üzgünüm kaybettiniz... ")
                yanlis += 1
    elif seviye == 2:
        islem = random.choice(list)
        sayi1 = random.randint (0, 9)
        sayi2 = random.randint (0, 9)
        if islem == "+":
            sonuc = sayi1+sayi2
        elif islem == "-":
            sonuc = sayi1-sayi2
        elif islem == "*":
            sonuc = sayi1*sayi2
        else:
            if sayi2 == 0: #Sayı sıfıra bölünürse hata alır!
                sonuc =  sayi2/sayi1
                sayi1, sayi2 = sayi2, sayi1
            else:
                sonuc = sayi1/sayi2
        for i in range (4, -1, -1):
            kullanici = int (input ("{} {} {} = ".format (sayi1, islem, sayi2)))
            if kullanici == sonuc:
                puan += 20
                print ("Tebrikler.. Puanınız : {}".format (puan))
                dogru += 1
                break
            elif i > 0:
                puan -= 4
                print ("Tekrar deneyiniz ,puanınız {} ve kalan hakkınız {}".format (puan, i))
                yanlis += 1
            else:
                print ("Üzgünüm kaybettiniz...")
                yanlis += 1
    elif seviye == 3:
        islem = random.choice(list)
        sayi1 = random.randint (0, 99)
        sayi2 = random.randint (0, 99)
        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        else:
            if sayi2 == 0:  # Sayı sıfıra bölünürse hata alır!
                sonuc = sayi2 / sayi1
                sayi1,sayi2 = sayi2,sayi1
            else:
                sonuc = sayi1 / sayi2
        for i in range (3, -1, -1):
            kullanici = int (input ("{} {} {} = ".format (sayi1, islem, sayi2)))
            if kullanici == sonuc:
                puan += 30
                print ("Tebrikler.. Puanınız : {}".format (puan))
                dogru += 1
                break
            elif i > 0:
                puan -= 6
                print ("Tekrar deneyiniz ,puanınız {} ve kalan hakkınız {}".format (puan, i))
                yanlis += 1
            else:
                print ("Üzgünüm kaybettiniz...")
                yanlis += 1
    elif seviye == 4:
        islem = random.choice(list)
        sayi1 = random.randint (0, 999)
        sayi2 = random.randint (0, 999)
        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        else:
            if sayi2 == 0:  # Sayı sıfıra bölünürse hata alır!
                sonuc = sayi2 / sayi1
                sayi1, sayi2 = sayi2, sayi1
            else:
                sonuc = sayi1 / sayi2
        for i in range (2, -1, -1):
            kullanici = int (input ("{} {} {} = ".format (sayi1, islem, sayi2)))
            if kullanici == sonuc:
                puan += 50
                print ("Tebrikler.. Puanınız : {}".format (puan))
                dogru += 1
                break
            elif i > 0:
                puan -= 10
                print ("Tekrar deneyiniz ,puanınız {} ve kalan hakkınız {}".format (puan, i))
                yanlis += 1
            else:
                print ("Üzgünüm kaybettiniz...")
                yanlis += 1
    elif seviye == 5:
        if puan > 200:
            print ("-" * 30)
            print("Tebriklerr, puanınız : {}".format(puan))
        else:
            print ("-" * 30)
            print("Çalışmaya devam edin, puanınız : {} ".format(puan))
        toplamsoru=dogru+yanlis
        yuzde = (dogru/toplamsoru)*100
        print ("Bugün {} sorudan {} tanesini doğru , {} tanesini yanlış cevaplayarak %{} başarı elde ettiniz...".format(toplamsoru,dogru,yanlis,yuzde))
        break
    else:
        print("-"*30)
        print("Geçerli bir değer girilmemiştir. Lütfen tekrar deneyiniz...")
        print("-"*30)