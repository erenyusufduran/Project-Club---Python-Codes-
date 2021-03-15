# Kütüphanler
import random
import time
import sys


# KolayMod Fonksiyonlar
def kolay_mod_toplama():
    print("Toplama işlemi seçildi! Sorun geliyor.")
    sayi1 = random.randint(0, 10)
    sayi2 = random.randint(0, 10)
    sonuc = sayi1 + sayi2
    try:
        cevap = int(input("{} + {} işleminin sonucu kaçtır?\nSorudan çıkmak için [00] yazın ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()

        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


def kolay_mod_cikarma():
    print("Çıkarma işlemi seçildi! Sorun geliyor.")
    sayi1 = random.randint(0, 10)
    sayi2 = random.randint(0, 10)
    sonuc = sayi1 - sayi2
    try:
        cevap = int(input("{} - {} işleminin sonucu kaçtır?\nSorudan çıkmak için [00] yazın' ".format(sayi1, sayi2)))

        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()
        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


def kolay_mod_carpma():
    print("Çarpma işlemi seçildi! Sorun geliyor.")
    sayi1 = random.randint(0, 10)
    sayi2 = random.randint(0, 10)
    sonuc = sayi1 * sayi2
    try:
        cevap = int(input("{} x {} işleminin sonucu kaçtır?\nSorudan çıkmak için [00] yazın ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()

        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


def kolay_mod_bolme():
    print("Bölme işlemi seçildi! Sorun geliyor.(Küsüratı yazmanıza gerek yok.)")
    sayi1 = random.randint(0, 10)
    sayi2 = random.randint(1, 10)  # ZeroDivisonError almamak için sayı aralığını 1 den aldım.
    sonuc = sayi1 // sayi2
    try:
        cevap = int(input("{} / {} işleminin sonucu kaçtır?\nSorudan çıkmak için [00] yazın ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()

        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


# OrtaMod Fonksiyonlar
def orta_mod_toplama():
    print("Toplama işlemi seçildi! Sorun geliyor.")
    sayi1 = random.randint(0, 50)
    sayi2 = random.randint(0, 50)
    sonuc = sayi1 + sayi2

    try:
        cevap = int(
            input("{} + {} işleminin sonucu kaçtır?\nUygulamadan çıkmak için [00] yazın. ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()

        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


def orta_mod_cikarma():
    print("Çıkarma işlemi seçildi! Sorun geliyor.")
    sayi1 = random.randint(0, 50)
    sayi2 = random.randint(0, 50)
    sonuc = sayi1 - sayi2
    try:
        cevap = int(input("{} - {} işleminin sonucu kaçtır?\nSourdan çıkmak için [00] yazın. ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()

        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


def orta_mod_carpma():
    print("Çarpma işlemi seçildi! Sorun geliyor.")
    sayi1 = random.randint(0, 50)
    sayi2 = random.randint(0, 50)
    sonuc = sayi1 * sayi2
    try:
        cevap = int(input("{} x {} işleminin sonucu kaçtır?\nSorudan çıkmak için [00] yazın. ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()

        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


def orta_mod_bolme():
    print("Bölme işlemi seçildi! Sorun geliyor.(Küsüratı yazmanıza gerek yok.)")
    sayi1 = random.randint(0, 50)
    sayi2 = random.randint(1, 50)  # ZeroDivision için yine
    sonuc = sayi1 // sayi2
    try:
        cevap = int(input("{} / {} işleminin sonucu kaçtır?\nSorudan çıkmak için [00] yazın. ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()

        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


# ZorMod Fonksiyonlar
def zor_mod_toplama():
    print("Toplama işlemi seçildi! Sorun geliyor.")
    sayi1 = random.randint(0, 100)
    sayi2 = random.randint(0, 100)
    sonuc = sayi1 + sayi2
    try:
        cevap = int(input("{} + {} işleminin sonucu kaçtır?\nSorudan çıkmak için [00] yazın. ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()

        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


def zor_mod_cikarma():
    print("Çıkarma işlemi seçildi! Sorun geliyor.")
    sayi1 = random.randint(0, 100)
    sayi2 = random.randint(0, 100)
    sonuc = sayi1 - sayi2
    try:
        cevap = int(input("{} - {} işleminin sonucu kaçtır?\nSorudan çıkmak için [00] yazın. ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()

        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


def zor_mod_carpma():
    print("Çarpma işlemi seçildi! Sorun geliyor.")
    sayi1 = random.randint(0, 100)
    sayi2 = random.randint(0, 100)
    sonuc = sayi1 * sayi2
    try:
        cevap = int(input("{} x {} işleminin sonucu kaçtır?\nSorudan çıkmak için [00] yazın. ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")

        elif cevap == 00:
            print("Uygulamadan çıkılıyor...")
            time.sleep(2)
            sys.exit()
        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


def zor_mod_bolme():
    print("Bölme işlemi seçildi! Sorun geliyor.(Küsüratı yazmanıza gerek yok.)")
    sayi1 = random.randint(0, 100)
    sayi2 = random.randint(1, 100)  # Artık biliyosunuz olayı :P
    sonuc = sayi1 // sayi2
    try:
        cevap = int(input("{} / {} işleminin sonucu kaçtır?\nSorudan çıkmak için [00] yazın. ".format(sayi1, sayi2)))
        if cevap == sonuc:
            print("DOĞRU CEVAP!!")
        else:
            print("YANLIŞ CEVAP!! Oyun bitti..")
            time.sleep(3)
            sys.exit()

    except ValueError:
        print("Hatalı değer girdiniz.\nUygulamadan Çıkılıyor")
        time.sleep(2)
        sys.exit()


# Döngü Kısmı

# ----------------------------------------------------------------------------------------------------------------------
print(
    "===================================$$İŞLEM OYUNUNA HOŞ GELDİNİZ$$=====================================".center(100,
                                                                                                                    '*'))
while True:
    try:
        zorluk = int(input(
            "\n********************************\n**Zorluk Seçiniz:             ** \n**  -Kolay[1]                 "
            "**\n**  -Orta[2]                  **\n**  -Zor[3]                   "
            "**\n********************************\n**Kuralları görmek için:   [8]**\n**Çıkmak için:             ["
            "9]**\n********************************"))
    except ValueError:
        print("Geçersiz bir değer girdiniz.Lütfen tekrar deneyin")
        time.sleep(1)
        continue
    # ----------------------------------------------------------------------------------------------------------------------
    if zorluk == 1:
        print("Kolay mod seçildi\nUnutma tek bir hakkın var yanlış bilirsen kaybedersin..")
        try:
            islem = int(input("İşlem Seçiniz: Toplama[1], Çıkarma[2], Çarpma[3], Bölme[4]"))
        except ValueError:
            print("Geçersiz bir değer girdiniz.Lütfen tekrar deneyin")
            time.sleep(1)

        if islem == 1:
            while True:
                kolay_mod_toplama()
        elif islem == 2:
            while True:
                kolay_mod_cikarma()
        elif islem == 3:
            while True:
                kolay_mod_carpma()
        elif islem == 4:
            while True:
                kolay_mod_bolme()

    # ----------------------------------------------------------------------------------------------------------------------
    if zorluk == 2:
        print("Orta mod seçildi\nUnutma tek bir hakkın var yanlış bilirsen kaybedersin..")
        try:
            islem = int(input("İşlem Seçiniz: Toplama[1], Çıkarma[2], Çarpma[3], Bölme[4]"))
        except ValueError:
            print("Geçersiz bir değer girdiniz.Lütfen tekrar deneyin")
            time.sleep(1)
            continue

        if islem == 1:
            while True:
                orta_mod_toplama()
        elif islem == 2:
            while True:
                orta_mod_cikarma()
        elif islem == 3:
            while True:
                orta_mod_carpma()
        elif islem == 4:
            while True:
                orta_mod_bolme()

    # ----------------------------------------------------------------------------------------------------------------------
    if zorluk == 3:
        print("Zor mod seçildi\nUnutma tek bir hakkın var yanlış bilirsen kaybedersin..")
        try:
            islem = int(input("İşlem Seçiniz: Toplama[1], Çıkarma[2], Çarpma[3], Bölme[4]"))
        except ValueError:
            print("Geçersiz bir değer girdiniz.Lütfen tekrar deneyin")
            time.sleep(1)
            continue

        if islem == 1:
            while True:
                zor_mod_toplama()
        elif islem == 2:
            while True:
                zor_mod_cikarma()
        elif islem == 3:
            while True:
                zor_mod_carpma()
        elif islem == 4:
            while True:
                zor_mod_bolme()
    # ----------------------------------------------------------------------------------------------------------------------
    if zorluk == 9:
        print("Uygulamadan Çıkılıyor..")
        time.sleep(3)
        sys.exit()
    # ----------------------------------------------------------------------------------------------------------------------
    if zorluk == 8:
        print("--Cevabı doğru tahmin etmek için 1 hakkın var.Bilirsen devam edersin yoksa elenirsin.")
        print("--Bölme işlemlerinde cevap tamsayı olarak istenir.Küsürat yazmanıza gerek yoktur.")

        time.sleep(5)