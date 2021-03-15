#Bu program Beykent Üniversitesi Proje Üretim Kulübü etkinliği için Oğuz Özdemir tarafından yazılmıştır.

import random

i = 0
puan = 0
seviye = 1
sonrakiSeviyeKolay = 50
sonrakiSeviyeOrta = 70
sonrakiSeviyeZor = 100
print("""################################################################
        ZORLUKLARLA MATEMATİK OYUNUNA HOŞGELDİNİZ!
################################################################


""")
baslangic = input("Oyunu başlatmak için [Başlat], çıkış yapmak için [Çıkış], kurallar için [Kurallar] yazman yeterli: ")

while True:
    if baslangic in ("Çıkış", "çıkış", "cikis", "Cikis", "çıkıs"):
        print("Çıkış yapılıyor...")
        exit()


    elif baslangic in ("Kurallar", "kurallar", "KURALLAR"):
        print("""################################################################ 
                     KURALLAR 
################################################################

        1.İşlemleri doğru bilerek puanları topla ve bir sonraki seviyeye geç! 
        2.Seçtiğin zorluğa göre yanlış yazma hakkına sahipsin. İşlemleri yaparken iyi düşün, skorunu kaybetme! 
        3.İstediğin zaman [Çıkış] yazarak oyundan çıkma hakkına sahipsin ama skorunun kaydedilmediğini unutma! 
        4.Eğlenirken matematik işlem kabiliyetini geliştir ve pratikleştir! 
        """)
        baslangic = input("Oyuna başlamak için [Başlat], çıkış yapmak için [Çıkış] yazman yeterli: ")

    elif baslangic in ("Başlat", "başlat", "baslat", "Baslat", "BAŞLAT", "BASLAT"):
        break

    else:
        baslangic = input("Seçimini anlayamadık, [Başlat], [Çıkış] veya [Kurallar] seçimlerinden birini yap: ")

zorluk = input(
    "Zorluk seçiminiz: \n\t Kolay: Toplama ve çıkarma işlemleri, 5 yanlış yazma hakkı. Bir sonraki seviye için 50 puana ulaş. \n\t Orta: Toplama, çıkarma, çarpma ve bölme işlemleri, 3 yanlış yazma hakkı. Her yanlışta 2 puan kaybedilir. Bir sonraki seviye için 70 puana ulaş. \n\t Zor: Toplama, çıkarma, çarpma, bölme ve üslü sayılar, 1 yanlış yazma hakkı. Her yanlışta 5 puan kaybedilir. Bir sonraki seviye için 100 puana ulaş. \n\t Seçiminiz: ")
while True:  # zorluk secimi

    if zorluk in ("Kolay", "kolay", "KOLAY"):
        n = 5
        b = 1
        break
    elif zorluk in ("Orta", "orta", "ORTA"):
        n = 3
        b = 2
        break
    elif zorluk in ("Zor", "zor", "ZOR"):
        n = 2
        b = 3
        break
    elif zorluk in ("Çıkış", "çıkış", "cikis", "Cikis", "çıkıs"):
            print("Çıkış yapılıyor...")
            exit()
    else:
        zorluk = input("Seçimini anlayamadık, [Kolay], [Orta] veya [Zor] seçimlerinden birini yap: ")

while i < n:

    sayi1 = random.randint(1, 50)
    sayi2 = random.randint(1, 50)
    sayi3 = random.randint(1, 20)
    sayi4 = random.randint(1, 50)
    sayi5 = random.randint(1, 50)
    uslu = random.randint(1, 5)

    if b == 1:  # kolay

        if sayi3 in (1, 2,3,4,5,6,7,8,9,10):
            sonuc = sayi1 + sayi2
            islem = "+"
            cevap = input("{}{}{} işleminin cevabı kaçtır? ".format(sayi1, islem, sayi2))
        if sayi3 in (11,12,13,14,15,16,17,18,19,20):
            sonuc = sayi1 - sayi2
            islem = "-"
            cevap = input("{}{}{} işleminin cevabı kaçtır? ".format(sayi1, islem, sayi2))


        if cevap in ("çıkış","cikis","ÇIKIŞ","CİKİS","cikiş","ÇİKİŞ","Çıkış"):
            print = input("Puanınız: {} \n\tSeviyeniz: {}\n\tÇıkış yapılıyor...".format(puan,seviye))
            exit()

        try:
            try:
                cevap = int(cevap)
            except:
                print("Lütfen geçerli bir değer giriniz.")
            if cevap == sonuc:
                print("Tebrikler, bildin!")
                puan = puan + 10
                while puan >= sonrakiSeviyeKolay:
                    seviye += 1
                    puan = puan - sonrakiSeviye
                    sonrakiSeviye = round(sonrakiSeviyeKolay * 1.5)
            else:
                print("Bilemedin!")
                i = i + 1

                while puan >= sonrakiSeviyeKolay:
                    seviye += 1
                    puan = puan - sonrakiSeviyeKolay
                    sonrakiSeviye = round(sonrakiSeviyeKolay * 1.5)

                if n - i == 0:
                    print("Hakkın kalmadı.")

                else:
                    print(n - i, "Hakkın kaldı.")

            print("Puanınız: {}".format(puan))
            print("Seviye: ", seviye)
            print("Puan: ", puan)
            print("Sonraki Seviye: ", sonrakiSeviyeKolay)

            if cevap in ("çıkış","cikis","ÇIKIŞ","CİKİS","cikiş","ÇİKİŞ","Çıkış"):
                print("Çıkış yapılıyor...")
                exit()
        except:
            0


    elif b == 2:  # orta

        if sayi3 in (1, 2,18,19):
            sonuc = sayi1 + sayi2
            islem = "+"
            cevap = input("{}{}{}{}{} işleminin cevabı kaçtır? ".format(sayi1, islem, sayi2, islem,sayi4 ))
        if sayi3 in (3, 4,17,20):
            sonuc = sayi1 - sayi2
            islem = "-"
            cevap = input("{}{}{}{}{}{}{} işleminin cevabı kaçtır? ".format(sayi1, islem, sayi2,islem,sayi4,islem,sayi5))
        if sayi3 in (5, 6, 7,14,15,16):
            sonuc = sayi1 * sayi2
            islem = "*"
            cevap = input("{}{}{} işleminin cevabı kaçtır? ".format(sayi1, islem, sayi2))

        if sayi3 in (8, 9, 10,11,12,13):
            sonuc = sayi1
            islem = "/"
            cevap = input("{}{}{} işleminin cevabı kaçtır? ".format((sayi1 * sayi2), islem, sayi2))

        if cevap in ("çıkış","cikis","ÇIKIŞ","CİKİS","cikiş","ÇİKİŞ","Çıkış"):
            print = input("Puanınız: {} \n\tSeviyeniz: {}\n\tÇıkış yapılıyor...".format(puan,seviye))
            exit()

        try:
            try:
                cevap = int(cevap)
            except:
                print("Lütfen geçerli bir değer giriniz.")
            if cevap == sonuc:
                print("Tebrikler, bildin!")
                puan = puan + 10
                while puan >= sonrakiSeviyeOrta:
                    seviye += 1
                    puan = puan - sonrakiSeviyeOrta
                    sonrakiSeviye = round(sonrakiSeviyeOrta * 1.5)
            else:
                print("Bilemedin!")
                i = i + 1
                puan = puan - 2
                while puan >= sonrakiSeviyeOrta:
                    seviye += 1
                    puan = puan - sonrakiSeviyeOrta
                    sonrakiSeviye = round(sonrakiSeviyeOrta * 1.5)

                if n - i == 0:
                    print("Hakkın kalmadı.")

                else:
                    print(n - i, "Hakkın kaldı.")

            print("Puanınız: {}".format(puan))
            print("Seviye: ", seviye)
            print("Puan: ", puan)
            print("Sonraki Seviye: ", sonrakiSeviyeOrta)

            if cevap in ("çıkış","cikis","ÇIKIŞ","CİKİS","cikiş","ÇİKİŞ","Çıkış"):
                print("Çıkış yapılıyor...")
                exit()
        except:
            0

    elif b == 3:  # zor
        if sayi3 in (1, 2,3,4):
            sonuc = sayi1 + sayi2 + sayi4 + sayi5
            islem = "+"
            cevap = input("{}{}{}{}{}{}{} işleminin cevabı kaçtır? ".format(sayi1, islem, sayi2, islem, sayi4, islem, sayi5))
        if sayi3 in (5,6,7,8):
            sonuc = sayi1 - sayi2 - sayi4 - sayi5
            islem = "-"
            cevap = input("{}{}{}{}{}{}{} işleminin cevabı kaçtır? ".format(sayi1, islem, sayi2, islem, sayi4, islem, sayi5))
        if sayi3 in (9,10,11,12):
            sonuc = sayi1 * sayi2
            islem = "*"
            cevap = input("{}{}{} işleminin cevabı kaçtır? ".format(sayi1, islem, sayi2))

        if sayi3 in (13,14,15,16):
            sonuc = sayi1
            islem = "/"
            cevap = input("{}{}{} işleminin cevabı kaçtır? ".format((sayi1 * sayi2), islem, sayi2))

        if sayi3 in (17,18,19,20):
            sonuc = sayi1 ** uslu
            islem = "**"
            cevap = input("{}{}{} işleminin cevabı kaçtır?".format(sayi1, islem, uslu))

        if cevap in ("çıkış","cikis","ÇIKIŞ","CİKİS","cikiş","ÇİKİŞ","Çıkış"):
            print = input("Puanınız: {} \n\tSeviyeniz: {}\n\tÇıkış yapılıyor...".format(puan,seviye))
            exit()

        try:
            try:
                cevap = int(cevap)
            except:
                print("Lütfen geçerli bir değer giriniz.")
            if cevap == sonuc:
                print("Tebrikler, bildin!")
                puan = puan + 10
                while puan >= sonrakiSeviyeZor:
                    seviye += 1
                    puan = puan - sonrakiSeviyeZor
                    sonrakiSeviye = round(sonrakiSeviyeZor * 1.5)
            else:
                print("Bilemedin!")
                i = i + 1
                puan = puan - 5
                while puan >= sonrakiSeviyeZor:
                    seviye += 1
                    puan = puan - sonrakiSeviyeZor
                    sonrakiSeviye = round(sonrakiSeviyeZor * 1.5)

                if n - i == 0:
                    print("Hakkın kalmadı.")

                else:
                    print(n - i, "Hakkın kaldı.")
            print("Puanınız: {}".format(puan))
            print("Seviye: ", seviye)
            print("Puan: ", puan)
            print("Sonraki Seviye: ", sonrakiSeviyeZor)

            if cevap in ("çıkış","cikis","ÇIKIŞ","CİKİS","cikiş","ÇİKİŞ","Çıkış"):
                print("Çıkış yapılıyor...")
                exit()

        except:
            0