tahmin1=0
tahmin2=0
sonuc=0
zorluk_sev =0
import random
while True:
    cıkıs_devam=input("Lütfen devam etmek için herhangi bir tuşa basınız çıkmak için q tuşuna basınız.:")
    if cıkıs_devam == "Q" or cıkıs_devam == "q":
        break
    else:
        print ("işleme devam ediliyor")
    print("Zorluk seviyeleri:","toplama1=1-99 arası iki sayının toplamı","toplama2=100-999 arası iki sayının toplamı","toplama3=1000-9999 arası iki sayının toplamı","","çıkartma1=1-99 arası pozitif sonuçlu","çıkartma2=100-999 arası pozitif sonuçlu","çıkartma3=1000-9999 arası pozitif yada negatif sonuçlu","","çarpma1=1-9 arası iki sayının çarpımı","çarpma2=10-99 arası iki sayının çarpımı","çarpma3=100-999 arası iki sayının çarpımı","","bölme1=1-9 arası bölümün sonucu kalansız iki sayının birbirine bölümü","bölme2=10-99 arası iki sayının kalansız bölümü","bölme3=100-999 arası iki sayının kalansız bölümü",sep="\n")
    while True:
        zorluk_sev = int(input("Lütfen zorluk seviyesini seçiniz(1/3) : "))
        if zorluk_sev==1 or zorluk_sev==2 or zorluk_sev==3:
            print("zoruluğun seviyesi:",zorluk_sev,"olarak ayarlandı")
            break
        else:
            print ("böyle bir zorluk sevıyesı eklenmemiştir.")
                            #işlem için
    while True:
        islem=input("Lütfen yapılacak işlemi seçin Topla=T, Çıkar=F, Çarp=C, Bölme=B :")
        if (islem == "T") | (islem == "t"):
            if zorluk_sev==1:
                tahmin1= random.randint(1,99)
                tahmin2= random.randint(1,99)
            elif zorluk_sev==2:
                tahmin1= random.randint(100,999)
                tahmin2= random.randint(100,999)
            elif zorluk_sev==3:
                tahmin1= random.randint(1000,9999)
                tahmin2= random.randint(1000,9999)
            sonuc = tahmin1 + tahmin2
            islem="+"
            break
        elif islem == "F" or islem == "f":
            if zorluk_sev==1:
                while True:
                    tahmin1= random.randint(1,99)
                    tahmin2= random.randint(1,99)
                    if tahmin1>=tahmin2:
                        break
            elif zorluk_sev==2:
                while True:
                    tahmin1= random.randint(100,999)
                    tahmin2= random.randint(100,999)
                    if tahmin1>=tahmin2:
                        break
            elif zorluk_sev==3:
                tahmin1= random.randint(1000,9999)
                tahmin2= random.randint(1000,9999)
            sonuc = tahmin1 - tahmin2
            islem="-"
            break
        elif islem == "C" or islem == "c":
            if zorluk_sev==1:
                tahmin1= random.randint(1,9)
                tahmin2= random.randint(1,9)
            elif zorluk_sev==2:
                tahmin1= random.randint(10,99)
                tahmin2= random.randint(10,99)
            elif zorluk_sev==3:
                tahmin1= random.randint(100,999)
                tahmin2= random.randint(100,999)
            sonuc = tahmin1 * tahmin2
            islem="*"
            break
        elif islem == "B" or islem == "b":
            islem="/"
            if zorluk_sev==1:
                while True:
                    tahmin1= random.randint(1,9)
                    tahmin2= random.randint(1,9)
                    if tahmin1 % tahmin2 == 0:
                        break
            
                                    #kalansız bölünen iki adet tek basamaklı sayı
            elif zorluk_sev==2:
                while True:
                    tahmin1= random.randint(10,99)
                    tahmin2= random.randint(1,9)
                    if tahmin1 % tahmin2 == 0:
                        break
                                    #îki basamaklı bir sayıya kalansız bölünen tek basmaklı sayı
            elif zorluk_sev==3:
                while True:
                    tahmin1= random.randint(100,999)
                    tahmin2= random.randint(10,99)
                    if tahmin1 % tahmin2 == 0:
                        break
                                    #üç basamaklı bir sayıya tam bölünen tek basamaklı sayı
            
            if tahmin1 == 0 and tahmin2 == 0:
                sonuc = "0/0 durumu"
                break
            elif tahmin2 == 0:
                sonuc = "Sayının 0a bölümü tanımsızdır"
                break
            else:
                sonuc = tahmin1 / tahmin2
                break
        else:
            print("lütfen gecerli bir işlem türü giriniz")
    while True:
        print("{}{}{}=? sonucu kaçtır?".format(tahmin1,islem,tahmin2))
        cevap = int(input("lütfen sonucunuzu giriniz:"))
        if cevap != sonuc:
            print("yanlış cevap lütfen tekrar dene")
        elif cevap == sonuc:
            print("cevabın dogru")
            break
    