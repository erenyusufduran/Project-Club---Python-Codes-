# Proje: Bilgisayarın rastgele ürettiği iki sayı ve işlemin sonucunu kullanıcıya soran bir uygulama kodlama

import random

print(
    "Merhaba! Ben Seviyelerle Dört İşlem Uygulaması. Sana rastgele toplama, çıkarma, çarpma ve bölme işlemleri soracağım.")
print("BİLGİLENDİRME!!")
print("Programımız 4 seviyeden oluşmaktaktadır.")
print(
    "1. Seviyeyi geçmek için en az 30 puana sahip olmalısınız. Sorular 1-10 arası sayılardan oluşmaktadır. Doğru:3 PUAN , Yanlış: -1 PUAN ")
print(
    "2. Seviyeyi geçmek için en az 70 puana sahip olmalısınız. Sorular 10-100 arası sayılardan oluşmaktadır. Doğru:5 PUAN , Yanlış: -3 PUAN ")
print(
    "3. Seviyeyi geçmek için en az 120 puana sahip olmalısınız. Sorular 100-500 arası sayılardan oluşmaktadır. Doğru:8 PUAN , Yanlış: -5 PUAN")
print(
    "4. Seviyeye geçmek için en az 200 puana sahip olmalısınız. Sorular 100-1000 arası sayılardan oluşmaktadır. Doğru:12 PUAN , Yanlış: -7 PUAN")
print("")
print(" Hazırsan başlayalım :)\n")

puan = 0

cevap = "1"
while cevap == "1":

    if puan >= 0 and puan <= 30:
        birincisayi = random.randint(1, 10)
        ikincisayi = random.randint(1, 10)
        islemler = random.randint(1, 4)

        if islemler == 1:
            sonuc = birincisayi + ikincisayi
            soru = int(input("{} + {} = ? işleminin sonucu kaçtır?.".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 3
                print("Harika! Doğru Cevap. Puanın:{}".format(puan))
            else:
                puan = puan - 1
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 2:
            sonuc = birincisayi - ikincisayi
            soru = int(input("{} - {} = ? işleminin sonucu kaçtır?".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 3
                print("Harika! Doğru Cevap. Puanın:{}".format(puan))
            else:
                puan = puan - 1
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 3:
            sonuc = birincisayi * ikincisayi
            soru = int(input("{} * {} = ? işleminin sonucu kaçtır?".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 3
                print("Harika! Doğru Cevap. Puanın:{}".format(puan))
            else:
                puan = puan - 1
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 4:
            sonuc = birincisayi // ikincisayi
            soru = int(input("{} / {} = ? işleminin sonucu kaçtır?".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 3
                print("Harika! Doğru Cevap. Puanın:{}".format(puan))
            else:
                puan = puan - 1
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        print("İşlemleri yanıtlamaya devam etmek ister misin?")
        cevap = input("Yanıtınız evet ise [1], hayır ise [2] tuşuna basınız:")
        if cevap == "2":
            print("Daha Sonra Tekrar Beklerim ^_^")

        if puan > 30 and puan < 70:
            print("")
            print("______________TEBRİK EDERİM 2.SEVİYEYE HOŞGELDİN_____________")
        print("")

    elif puan >= 31 and puan <= 70:
        birincisayi = random.randint(10, 100)
        ikincisayi = random.randint(10, 100)
        islemler = random.randint(1, 4)

        if islemler == 1:
            sonuc = birincisayi + ikincisayi
            soru = int(input("{} + {} = ? işleminin sonucu kaçtır?.".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 5
                print("Mükemmel Böyle Devam :) Puanın:{}".format(puan))
            else:
                puan = puan - 3
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 2:
            sonuc = birincisayi - ikincisayi
            soru = int(input("{} - {} = ? işleminin sonucu kaçtır?".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 5
                print("Mükemmel Böyle Devam :) Puanın:{}".format(puan))
            else:
                puan = puan - 3
                print("Maalesef Yanlış Cevap.Puanın:{}".format(puan))

        elif islemler == 3:
            sonuc = birincisayi * ikincisayi
            soru = int(input("{} * {} = ? işleminin sonucu kaçtır?".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 5
                print("Mükemmel Böyle Devam :) Puanın:{}".format(puan))
            else:
                puan = puan - 3
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 4:
            sonuc = birincisayi // ikincisayi
            soru = int(input("{} / {} = ? işleminin sonucu kaçtır?".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 5
                print("Mükemmel Böyle Devam :) Puanın:{}".format(puan))
            else:
                puan = puan - 3
                print("Maalesef Yanlış Cevap.Puanın:{}".format(puan))

            print("İşlemleri yanıtlamaya devam etmek ister misin?")
        cevap = input("Yanıtınız evet ise [1], hayır ise [2] tuşuna basınız:")
        if cevap == "2":
            print("Daha Sonra Tekrar Beklerim ^_^")

        if puan > 70 and puan < 120:
            print("")
            print("______________TEBRİK EDERİM 3.SEVİYEYE HOŞGELDİN_____________")
        print("")

    elif puan >= 71 and puan <= 120:
        birincisayi = random.randint(100, 500)
        ikincisayi = random.randint(100, 500)
        islemler = random.randint(1, 4)

        if islemler == 1:
            sonuc = birincisayi + ikincisayi
            soru = int(input("{} + {} = ? işleminin sonucu kaçtır?.".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 8
                print("Çok İyi Gidiyorsun. Puanın:{}".format(puan))
            else:
                puan = puan - 5
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 2:
            sonuc = birincisayi - ikincisayi
            soru = int(input("{} - {} = ? işleminin sonucu kaçtır?.".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 8
                print("Çok İyi Gidiyorsun. Puanın:{}".format(puan))
            else:
                puan = puan - 5
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 3:
            sonuc = birincisayi * ikincisayi
            soru = int(input("{} * {} = ? işleminin sonucu kaçtır?.".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 8
                print("Çok İyi Gidiyorsun. Puanın:{}".format(puan))
            else:
                puan = puan - 5
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 4:
            sonuc = birincisayi // ikincisayi
            soru = int(input("{} / {} = ? işleminin sonucu kaçtır?.".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 8
                print("Çok İyi Gidiyorsun. Puanın:{}".format(puan))
            else:
                puan = puan - 5
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

            print("İşlemleri yanıtlamaya devam etmek ister misin?")
        cevap = input("Yanıtınız evet ise [1], hayır ise [2] tuşuna basınız:")
        if cevap == "2":
            print("Daha Sonra Tekrar Beklerim ^_^")

        if puan > 30 and puan < 70:
            print("")
            print("______________TEBRİK EDERİM 2.SEVİYEYE HOŞGELDİN_____________")
        print("")

    elif puan >= 121 and puan <= 200:
        birincisayi = random.randint(100, 1000)
        ikincisayi = random.randint(100, 1000)
        islemler = random.randint(1, 4)

        if islemler == 1:
            sonuc = birincisayi + ikincisayi
            soru = int(input("{} + {} = ? işleminin sonucu kaçtır?.".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 12
                print("Aynen Öyle! Puanın:{}".format(puan))
            else:
                puan = puan - 7
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 2:
            sonuc = birincisayi - ikincisayi
            soru = int(input("{} - {} = ? işleminin sonucu kaçtır?.".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 12
                print("Aynen Öyle! Puanın:{}".format(puan))
            else:
                puan = puan - 7
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 3:
            sonuc = birincisayi * ikincisayi
            soru = int(input("{} * {} = ? işleminin sonucu kaçtır?.".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 12
                print("Aynen Öyle! Puanın:{}".format(puan))
            else:
                puan = puan - 7
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

        elif islemler == 4:
            sonuc = birincisayi // ikincisayi
            soru = int(input("{} / {} = ? işleminin sonucu kaçtır?.".format(birincisayi, ikincisayi)))
            if sonuc == soru:
                puan = puan + 12
                print("Aynen Öyle! Puanın:{}".format(puan))
            else:
                puan = puan - 7
                print("Maalesef Yanlış Cevap. Puanın:{}".format(puan))

            print("İşlemleri yanıtlamaya devam etmek ister misin?")
        cevap = input("Yanıtınız evet ise [1], hayır ise [2] tuşuna basınız:")
        if cevap == "2":
            print("Daha Sonra Tekrar Beklerim ^_^")
