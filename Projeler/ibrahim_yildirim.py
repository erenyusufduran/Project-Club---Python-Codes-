import random

print("""
▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄         
▀▄▀                                 Merhaba oyuncu, oyunuma hoş geldin                                       ▄▀▄
▀▄▀             100 saniye süren, 10 sayine sonra başlayacak ve bitene kadar oyun devam edecek               ▄▀▄
▀▄▀                     Dogru bildigin her tahmin sana ekstra süre kazandiracak                              ▄▀▄
▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄                                            
""")


istek = "e"
while istek == "e":
    import time
    for x in range(10, 0, -1):
        print(x)
        time.sleep(1)
    seviye = 1
    puan = 1
    bitis = 0
    from time import *
    baslangic = round(perf_counter(), 2)
    sure = 0
    if seviye == 1:
        print("""
               ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
               ▀▄▀ 1. Seviye = 1 ile 20 arasinda bir sayi tutuyorum...▄▀▄
               ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
               """)
        sayi = random.randint(1, 20)
        while sure <=100 and seviye == 1:
            tahmin = int(input("Tuttugum sayiyi tahmin et: "))
            bitis = round(perf_counter(), 2)
            sure = bitis - baslangic
            print(round(sure,2))
            if sayi == tahmin:
                sure -= 5
                print("Tebrikler 5 sn kazandiniz. Suan ki süreniz: ", round(sure,2))
                puan += 1
                seviye = 2
            elif sayi > tahmin:
                print("Daha büyük")
            else:
                print("Daha kücük")


    if seviye == 2:
        print("""
               ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
               ▀▄▀ 2. Seviye = 1 ile 40 arasinda bir sayi tutuyorum...▄▀▄
               ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
                """)
        sayi = random.randint(1, 40)
        while sure <=100 and seviye ==2:
            tahmin = int(input("Tuttugum sayiyi tahmin et: "))
            bitis = round(perf_counter(), 2)
            sure = bitis - baslangic
            print(round(sure,2))
            if sayi == tahmin:
                sure -= 10
                print("Tebikler 10 sn kazandiniz. Suan ki süreniz: ", round(sure,2))
                puan += 1
                seviye = 3
            elif sayi > tahmin:
                print("Daha büyük")
            else:
                print("Daha kücük")

    if seviye == 3:
        print("""
              ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
              ▀▄▀ 3. Seviye = 1 ile 60 arasinda bir sayi tutuyorum...▄▀▄
              ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
              """)
        sayi = random.randint(1, 60)
        while sure <=100 and seviye ==3:
            tahmin = int(input("Tuttugum sayiyi tahmin et: "))
            bitis = round(perf_counter(), 2)
            sure = bitis - baslangic
            print(round(sure,2))
            if sayi == tahmin:
                sure -= 10
                print("Tebikler 10 sn kazandiniz. Suan ki süreniz: ", round(sure,2))
                puan += 1
                seviye = 4
            elif sayi > tahmin:
                print("Daha büyük")
            else:
                print("Daha kücük")

    if seviye == 4:
        print("""
               ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
               ▀▄▀ 4. Seviye = 1 ile 80 arasinda bir sayi tutuyorum...▄▀▄
               ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
               """)
        sayi = random.randint(1, 80)
        while sure <=100 and seviye ==4:
            tahmin = int(input("Tuttugum sayiyi tahmin et: "))
            bitis = round(perf_counter(), 2)
            sure = bitis - baslangic
            print(round(sure,2))
            if sayi == tahmin:
                sure -= 15
                print("Tebikler 15 sn kazandiniz. Suan ki süreniz: ", round(sure,2))
                puan += 1
                seviye = 5
            elif sayi > tahmin:
                print("Daha büyük")
            else:
                print("Daha kücük")

    if seviye == 5:
        print("""
               ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
               ▀▄▀ 5. Seviye = 1 ile 100 arasinda bir sayi tutuyorum... ▄▀▄
               ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
               """)
        sayi = random.randint(1, 100)
        while sure <=100 and seviye ==5:
            tahmin = int(input("Tuttugum sayiyi tahmin et: "))
            bitis = round(perf_counter(), 2)
            sure = bitis - baslangic
            print(round(sure,2))
            if sayi == tahmin:
                sure -= 20
                print("Tebikler 20 sn kazandiniz. Suan ki süreniz: ", round(sure,2))
                puan += 1
                seviye = 6
            elif sayi > tahmin:
                print("Daha büyük")
            else:
                print("Daha kücük")

        if seviye == 6:
            print("""
                 ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀
                 ▀▄▀  Son Seviye = 1 ile 200 arasinda bir sayi tutuyorum...  ▀▄▀
                 ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀
                 """)
            sayi = random.randint(1, 200)
            while sure <=100:
                tahmin = int(input("Tuttugum sayiyi tahmin et: "))
                bitis = round(perf_counter(), 2)
                sure = bitis - baslangic
                print(round(sure,2))
                if sayi == tahmin:
                    sure -= 25
                    print("Tebikler 25 sn kazandiniz. Suan ki süreniz: ", round(sure,2))
                    print("""
                           ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀
                           ▀▄▀  Son Seviye = 1 ile 200 arasinda bir sayi tutuyorum...  ▀▄▀
                           ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀
                        """)
                    sayi = random.randint(1, 200)
                    puan += 2
                elif sayi > tahmin:
                    print("Daha büyük")
                else:
                    print("Daha kücük")
    puan = seviye * puan * 10
    print("""
             ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
             ▀▄▀            TEBRİKLER SENDEN HIZLISI YOK            ▄▀▄
             ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
          """)
    print("🏆 PUANIN: ", puan, " 🏆")
    seviye = 0

    if (seviye == 0):
        istek = input("Oyunu tekrar oynamak istiyorsan [e]vet, istemiyorsan [h]ayır tuslayabilirsin: ")
        if (istek == "e"):
            print("Bu sefer daha iyisini yapabilirsin...")
        else:
            print("Oyunu oynadigin icin tesekkür ederim.")