#Proje: Bilgisayarın rastgele ürettiği iki sayı ve işlemin sonucunu kullanıcıya soran uygulamayı kodlamak.
# Programı Geliştiren: Gizem Duygu Sönmez

import random
MAX_TEKRAR_TUR_SAY = 3  # Oyunda bir soru üç turdan fazla tahmin edilmeye çalışılmış ve sonuç hala bulunamamışsa kesinti yapılır. Bu sayı daha sonra değiştirilebilir.
KESINTI_PUANI = 5       # Oyuncunun cevabı bulması 3 turu geçerse yapılacak olan kesinti puanı
ZORLUK_1_PUAN = 5
ZORLUK_2_PUAN = 10
ZORLUK_3_PUAN = 15
ZORLUK_4_PUAN = 20
ZORLUK_5_PUAN = 25
ZORLUK_6_PUAN = 30

oyuncu_var = True
print("Oyun kuralları:")
print("Bilgisayar tarafından rastgele üretilecek iki sayı için yapmak istediğiniz matematiksel işlemi ve zorluk seviyesini girmelisiniz.")
print("Zorluk seviyesi arttıkça doğru bildiğiniz her cevap için alacağınız puan da doğru orantılı olarak artacaktır.")
print("Ancak doğru sonucu bulmanız 3 turdan fazla sürdüyse puanınızda 5 puan kesinti olacaktır.")
print("oyunda evet cevapları için 'e' ya da 'E' ; hayır demek için 'h' ya da 'H' tuşlanmalıdır. ")
print("Oyuncu oyunu bitirince oyuncunun her turdaki puanlarının ve toplam puanının bulunduğu bir tablo oluşturulur.")
print("Başarılar!")

while oyuncu_var == True:
    tur_puanlari = []
    oyuncu_adi = input("Adınızı giriniz:")
    tur_sayisi = 0
    devam = True
    while devam == True:  # devam == True olduğu sürece döngü dönecektir.
        tur_sayisi += 1
        print("Zorluk seviyesini seçiniz:")
        print("1.Seviye: Sayılar 1-10 aralığında üretilir ve işlem toplama ya da çıkartma olabilir.")
        print("2.Seviye: Sayılar 1-10 aralığında üretilir ve işlem çarpma ya da bölme olabilir.")
        print("3.Seviye: Sayılar 1-100 aralığında üretilir ve işlem toplama ya da çıkartma olabilir.")
        print("4.Seviye: Sayılar 1-100 aralığında üretilir ve işlem çarpma ya da bölme olabilir.")
        print("5.Seviye: Sayılar 1-1000 aralığında üretilir ve işlem toplama ya da çıkartma olabilir.")
        print("6.Seviye: Sayılar 1-1000 aralığında üretilir ve işlem çarpma ya da bölme olabilir.")
        print("Seçtiğiniz zorluk seviyesi için seviye numarasını tuşlayınız (1 / 2 / 3 / 4 / 5 / 6):", end='')
        zorluk = int(input())
        while zorluk not in [1, 2, 3, 4, 5, 6]:
            zorluk = int(input("Hatalı veri girişi yaptınız. Zorluk seviyesi için 1,2 ya da 3 değerlerinden birini girmelisiniz! Tekrar giriniz:"))

        if zorluk == 1:
            birinci_sayi = random.randint(1, 10)
            ikinci_sayi = random.randint(1, 10)
            islem = input("Gerçekleştirmek istediğiniz işlemi giriniz(+ ya da -):")
            while islem not in ["+", "-"]:
                islem = input("Girmiş olduğunuz işlem gerçekleştirilemiyor! Bu zorluk seviyesinde yalnızca toplama ya da çıkartma yapılabilir.Lütfen tekrar giriniz:")

        elif zorluk == 2:
            birinci_sayi = random.randint(1, 10)
            ikinci_sayi = random.randint(1, 10)
            islem = input("Gerçekleştirmek istediğiniz işlemi giriniz(* ya da /):")
            while islem not in ["*", "/"]:
                islem = input("Girmiş olduğunuz işlem gerçekleştirilemiyor! Bu zorluk seviyesinde yalnızca toplama ya da çıkartma yapılabilir.Lütfen tekrar giriniz:")
            if islem == "/":
                print("Gireceğiniz cevap ondalıklı ise ondalıklı kısım iki basamak olacak şekilde giriş yapmanız gerekmektedir!")

        elif zorluk == 3:
            birinci_sayi = random.randint(1, 100)
            ikinci_sayi = random.randint(1, 100)
            islem = input("Gerçekleştirme istediğiniz işlemi giriniz(+ ya da -):")
            while islem not in ["+", "-"]:
                islem = input("Girmiş olduğunuz işlem gerçekleştirilemiyor! Bu zorluk seviyesinde yalnızca toplama ve çıkartma yapılabilir.Lütfen tekrar giriniz:")

        elif zorluk == 4:
            birinci_sayi = random.randint(1, 100)
            ikinci_sayi = random.randint(1, 100)
            islem = input("Gerçekleştirmek istediğiniz işlemi giriniz(* ya da /):")
            while islem not in ["*", "/"]:
                islem = input("Girmiş olduğunuz işlem gerçekleştirilemiyor! Bu zorluk seviyesinde yalnızca çarpma ve bölme yapılabilir.Lütfen tekrar giriniz:")
            if islem == "/":
                print("Gireceğiniz cevap ondalıklı ise ondalıklı kısım iki basamak olacak şekilde giriş yapmanız gerekmektedir!")

        elif zorluk == 5:
            birinci_sayi = random.randint(1, 1000)
            ikinci_sayi = random.randint(1, 1000)
            islem = input("Gerçekleştirmek istediğiniz işlemi giriniz(+ ya da -):")
            while islem not in ["+", "-"]:
                islem = input("Girmiş olduğunuz işlem gerçekleştirilemiyor! Bu zorluk seviyesinde yalnızca toplama ya da çıkartma yapılabilir.Lütfen tekrar giriniz:")
        else:
            birinci_sayi = random.randint(1, 1000)
            ikinci_sayi = random.randint(1, 1000)
            islem = input("Gerçekleştirme istediğiniz işlemi giriniz(* ya da / ):")
            while islem not in ["*", "/"]:
                islem = input("Girmiş olduğunuz işlem gerçekleştirilemiyor! Bu zorluk seviyesinde yalnızca çarpma ya da bölme yapılabilir.Lütfen tekrar giriniz:")
            if islem == "/":
                print("Gireceğiniz cevap ondalıklı ise ondalıklı kısım iki basamak olacak şekilde giriş yapmanız gerekmektedir!")

        # Seçilen işleme göre sonucun kaç olacağı hesaplanılır.
        if islem == "+":
            sonuc = birinci_sayi + ikinci_sayi
        elif islem == "-":
            sonuc = birinci_sayi - ikinci_sayi
        elif islem == "*":
            sonuc = birinci_sayi * ikinci_sayi
        else:
            sonuc = float(format(birinci_sayi / ikinci_sayi, ".2f"))

        # Oyuncunun cevabı istenir.
        cevap = float(input("{} {} {} = ? isleminin sonucu kaçtir?".format(birinci_sayi, islem, ikinci_sayi)))

        if cevap == sonuc:   # Verilen cevap sonuca eşit ise if bloğuna girilir ve zorluk seviyesine göre puanlar belirlenir. Değilse else bloğuna gidilir.
            print("Tebrikler, bildiniz!")
            if zorluk == 1:
                tur_puanlari.append(ZORLUK_1_PUAN)
            elif zorluk == 2:
                tur_puanlari.append(ZORLUK_2_PUAN)
            elif zorluk == 3:
                tur_puanlari.append(ZORLUK_3_PUAN)
            elif zorluk == 4:
                tur_puanlari.append(ZORLUK_4_PUAN)
            elif zorluk == 5:
                tur_puanlari.append(ZORLUK_5_PUAN)
            else:
                tur_puanlari.append(ZORLUK_6_PUAN)

        else:
            tekrarla = True
            tekrarlama_sayisi = 1                                    # Sorunun ilk sorulduğunda tur birinci tur sayılır ve ilk turda oyuncu cevabı bilememiştir.
            while tekrarla == True:                                  # Oyuncu tekrar bu sorunun cevabını tahmin etmek istiyorsa bu döngüye girilir.
                print("Maalesef bilemediniz.")
                print("Tekrar tahmin etmek ister misiniz?", end='')  # Kullanıcıya tekrar bilmek isteyip istemediği sorulur.
                tahmin_tekrar = input()
                while tahmin_tekrar not in ["e", "E", "h", "H"]:     # Oyuncu evet demek için "e" ya da "E" ; hayır demek için "h" ya da "H" tuşlamalıdır.
                    tahmin_tekrar = input("Tekrar giriniz:")         # Oyuncu bunlardan birini tuşlamadıysa tekrar istenir.

                if tahmin_tekrar == "e" or tahmin_tekrar == "E":     # Tahmin için evet girildiyse if bloğu çalışır.
                    tekrarlama_sayisi += 1                           # Burada aynı soru kullanıcı tarafından tekrar cevaplanmak istendiği için tekraralan tur sayısı bir arttırılır.

                    cevap = float(input("{} {} {} = ? işleminin sonucu kaçtir?".format(birinci_sayi, islem, ikinci_sayi)))

                    if tekrarlama_sayisi > MAX_TEKRAR_TUR_SAY:       # Oyuncunu tahmini 3 turu geçmişse puan kesinti yapılır.
                        if cevap == sonuc:
                            print("Tebrikler, bildiniz! Ancak doğru sonucu bulmanız {} turu geçti kazandığınız puanda {} puan kesinti olacaktır! ".format(MAX_TEKRAR_TUR_SAY,KESINTI_PUANI))
                            tekrarla = False
                            if zorluk == 1:
                                tur_puanlari.append(ZORLUK_1_PUAN - KESINTI_PUANI)
                            elif zorluk == 2:
                                tur_puanlari.append(ZORLUK_2_PUAN - KESINTI_PUANI)
                            elif zorluk == 3:
                                tur_puanlari.append(ZORLUK_3_PUAN - KESINTI_PUANI)
                            elif zorluk == 4:
                                tur_puanlari.append(ZORLUK_4_PUAN - KESINTI_PUANI)
                            elif zorluk == 5:
                                tur_puanlari.append(ZORLUK_5_PUAN - KESINTI_PUANI)
                            else:
                                tur_puanlari.append(ZORLUK_6_PUAN - KESINTI_PUANI)

                    else:
                        if cevap == sonuc:
                            print("Tebrikler, bildiniz!")
                            tekrarla = False
                            if zorluk == 1:
                                tur_puanlari.append(ZORLUK_1_PUAN)
                            elif zorluk == 2:
                                tur_puanlari.append(ZORLUK_2_PUAN)
                            elif zorluk == 3:
                                tur_puanlari.append(ZORLUK_3_PUAN)
                            elif zorluk == 4:
                                tur_puanlari.append(ZORLUK_4_PUAN)
                            elif zorluk == 5:
                                tur_puanlari.append(ZORLUK_5_PUAN)
                            else:
                                tur_puanlari.append(ZORLUK_6_PUAN)

                else:
                    tekrarla = False
                    print("Cevap: {}".format(sonuc))
                    tur_puanlari.append(0)

        print("Devam edip başka bir işlem yapmak istiyor musunuz? (e,E,h,H):", end='')   # Oyuncuya başka bir işlem yapmak isteyip istemediği sorulur.
        tekrar = input()
        while tekrar not in ['e', 'E', 'h', 'H']:  # Bu karakterlerden biri girilmediyse while döngüye girilir.
            tekrar = input("Tekrar giriniz:")
        if tekrar == 'H' or tekrar == 'h':
            devam = False

    # Oyuncu ile ilgili bilgiler ekrana yazdırılır.
    print("Oyuncunun Adı", end='  ')
    for i in range(tur_sayisi):
        print("{}. Tur Puanı".format(i + 1), end='  ')
    print("Toplam Puan")

    print("-------------", end='  ')
    for i in range(tur_sayisi):
        print("------------", end='  ')
    print("-----------")

    toplam_puan = 0
    print(format(oyuncu_adi, "13"), end='  ')
    for i in range(tur_sayisi):
        print(format("{} Puan".format(tur_puanlari[i]), "12"), end='  ')
        toplam_puan += tur_puanlari[i]
    print("{} Puan".format(toplam_puan))

    baska = input("Başka oyuncu var mı?")   # Başka oyuncu olup olmadığı sorulur. Eğer başka bir oyuncu varsa ilk while döngüsüne tekrar girilir.
    if baska == 'h' or baska == 'H':
        oyuncu_var = False
