# Proje: Bilgisayarın rastgele ürettiği iki sayı ve işlemin sonucunu kullanıcıya soran uygulamayı kodlayınız.

import random  # Rastgele sayıları seçebilmek için kullanılan kütüphane
import os  # Ekranı silmek için kullanılan kütüphane
import time  # Ekranı belli bir süre durdurmak için kullanılan kütüphane


class Hesapla:  # Sınıfımız kod tekrarından kurtulmak için tasarlanmıştır

    def __init__(self, islem, sayi1, sayi2):  # initialize metodu olup gerekli parametreleri alır
        self.islem = islem
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def hesapla(self):  # Rastgele gelen sayıları rastgele gelen işlemle hesaplar
        if islem == '+':
            sonuc = sayi1 + sayi2  # Toplama işlemi
        elif islem == '-':
            sonuc = sayi1 - sayi2  # Çıkarma işlemi
        elif islem == '*':
            sonuc = sayi1 * sayi2  # Çarpma işlemi
        elif islem == '/':
            sonuc = sayi1 / sayi2  # Bölme işlemi
        else:
            sonuc = sayi1 ** sayi2  # Üs alma işlemi
        return (sonuc)  # sonuc değerini döndürür


puan = 0  # Puanın başlangıç değeri

while True:  # Kullanıcı devam etmek istediği sürece programda çalışmaya devam eder
    print("Zorluk seviyesini seçiniz")
    print("1. seviye (Her soru 10 puan)")
    print("2. seviye (Her soru 20 puan)")
    print("3. seviye (Her soru 30 puan)")
    zorluk = str(input("Seçiniz:"))

    if zorluk == "1":
        islemler = ['+', '-', '/', '*']

        sayi1 = random.randint(1, 10)  # Rastgele sayı seçimi
        sayi2 = random.randint(1, 10)  # Rastgele sayı seçimi
        islem = random.choice(islemler)  # Rastgele işlem seçimi
        h1 = Hesapla(islem, sayi1, sayi2)  # h1 nesnesi oluşturma
        sonuc = h1.hesapla()  # Hesaplamanın sonucunun sonuca aktarılması

    elif zorluk == "2":
        islemler = ['+', '-', '/', '*', '**']

        sayi1 = random.randint(1, 50)  # Rastgele sayı seçimi
        sayi2 = random.randint(1, 50)  # Rastgele sayı seçimi
        islem = random.choice(islemler)  # Rastgele işlem seçimi
        h1 = Hesapla(islem, sayi1, sayi2)  # h1 nesnesi oluşturma
        sonuc = h1.hesapla()  # Hesaplamanın sonucunun sonuca aktarılması

    elif zorluk == "3":
        islemler = ['+', '-', '/', '*', '**']

        sayi1 = random.randint(1, 100)  # Rastgele sayı seçimi
        sayi2 = random.randint(1, 100)  # Rastgele sayı seçimi
        islem = random.choice(islemler)  # Rastgele işlem seçimi
        h1 = Hesapla(islem, sayi1, sayi2)  # h1 nesnesi oluşturma
        sonuc = h1.hesapla()  # Hesaplamanın sonucunun sonuca aktarılması

    else:  # Kullanıcının olası olmayan bir seçim yapması sonucu uyarılması ve işlemi tekrar sorması
        os.system('clear')  # Ekranı temizler
        print("Lütfen geçerli bir işlem giriniz...!")
        time.sleep(1.5)  # Programı 1.5 saniyeliğine durdurur
        os.system('clear')  # Ekranı temizler
        continue  # Döngüyü baştan alır

    os.system('clear')  # Ekranı temizler

    while True:  # Geçerli bir cevap girilene kadar işlemi döndürür
        cevap = input(
            "{}{}{} işleminin sonucu kaçtır?\n".format(sayi1, islem, sayi2))  # Kullanıcıdan tahmini bir cevap ister

        try:  # sonuc ve cevap değişkenleri aynı değere sahip olsalar dahi değişken tipleri farklı olduğu için birbirlerinden farklı olarak algılanırlar. Burda amaç iki değişkeni de aynı değişken tipine çevirmek
            if islem == '/':
                cevap = float(cevap)  # Tip dönüşümü
            else:
                cevap = int(cevap)  # Tip dönüşümü
        except:  # Kullanıcı farklı bir değişken tipi girse bile uyarı verip programa yeniden dahil edilir
            os.system('clear')  # Ekranı temizler
            input("Lütfen geçerli bir cevap veriniz...!")
            os.system('clear')  # Ekranı temizler
            continue  # Döngüyü baştan alır
        break  # Döngüden çıkar

    if cevap == sonuc:  # Tahminin doğru olup olmadığını kontrol eder
        print("Tebrikler, bildin!")

        if zorluk == "1":  # Sorunun zorluğuna göre puan dağılımı
            puan += 10
        elif zorluk == "2":
            puan += 20
        else:
            puan += 30

    else:
        print("Bilemedin! Cevap", sonuc, "olacaktı!...")

    time.sleep(1.5)  # Programı 1.5 saniye durdurur

    print("Toplam puan:", puan)  # Toplam elde etmiş olduğumuz puanı gösterir

    time.sleep(1.5)  # Programı 1.5 saniye durdurur

    while True:  # Net bir cevap verene kadar soruyu yineler
        onay = str(input("Tamam mı Devam mı ? \n"))  # Kullanıcıya işleme devam edip edilmeyeceği sorulur

        os.system('clear')  # Ekranı temizler

        if onay == "Tamam" or onay == "tamam":  # Kullanıcının ne cevap verdiği kontrol edilir
            break  # Döngüden çıkar
        elif onay == "Devam" or onay == "devam":
            break  # Döngüden çıkar
        else:  # Eğer geçerli bir cevap verilmediyse uyarılır ve aynı soru yine sorulur
            input("Lütfen geçerli bir cevap veriniz...!")  # Enter'a basana kadar uyarıyı ekranda tutar
            os.system('clear')  # Ekranı temizler

    if onay == "Tamam" or onay == "tamam":  # Kullanıcı eğer tamam dediyse program sonlandırılır
        break  # Döngüden çıkar

    os.system('clear')  # Ekranı temizler

print("Toplam puan: {}".format(puan))  # Toplamda ne kadar puan kazandığını gösterir