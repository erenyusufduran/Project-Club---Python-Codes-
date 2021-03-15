import random

print("""
...  ▐≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣▌
...  ▐                                                                ▌
...  ▐                      ⫷ Oyuna Hoşgeldin! ⫸                     ▌
...  █                  ⋖  Oyun 5 Seviyeden oluşuyor  ⋗               █
...  █ ⋪ Toplam puanın seviyene göre kalan hak sayınla hesaplanıcak ⋫ █
...  ▐       ⊴ Elinden geldiğince yüksek puan toplanmaya çalış ⊵      ▌
...  ▐                                                                ▌
...  ▐≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣▌
... """)
ad = input(" Oyuncu Adınızı Giriniz ≡≡⫸ ")
restart = "e"

while (restart == "e" or restart == "E" or restart == "evet" or restart == "Evet"):
    puan = 0
    level = 1
    if (level == 1):
        print(" ★ 1. Seviye || 1-20 Arasında bir Sayı")
        sayi = random.randint(1, 20)
        hak = 10
        while(hak > 0) and (level == 1):
            print(" ❤ Kalan Hak ❤ =  ",hak)
            tahmin = 0
            while (0 >= tahmin or tahmin >= 21):
                tahmin= int(input("Tahmininizi Giriniz = "))
                if (0 >= tahmin or tahmin >= 21):
                    print("Lütfen 1 ile 20 arası bir sayı giriniz.")
            if (tahmin == sayi):
                print(" 🏆 Tebrikler 2.Seviyeye geçtiniz.")
                level = 2
            else:
                hak = hak-1
                if (tahmin > sayi):
                    print("Tahminin Sayıdan Daha Büyük")
                else:
                    print("Tahminin Sayıdan Daha Küçük")
        puan = puan + (hak * (level-1)) * 10
        if (hak == 0 ):
            cls = lambda: print('\n' * 100)
            cls()
            print("✘ Maalesef tahmin hakkın bitti ✘","\n✔ Doğru Cevap ≡≡⫸",sayi,"\nOyunu kaybettin",ad,"\n🏆 Kazandığın toplam puan ≡≡⫸ ",puan)
            level = 0

    if (level == 2):
        print(" ★✫ 2. Seviye || 1-25 Arasında bir Sayı")
        sayi = random.randint(1,25)
        hak = 8
        while(hak > 0) and (level == 2):
            print(" ❤ Kalan Hak ❤ =  ",hak)
            tahmin = 0
            while (0 >= tahmin or tahmin >= 26):
                tahmin = int(input("Tahmininizi Giriniz = "))
                if (0 >= tahmin or tahmin >= 26):
                    print("Lütfen 1 ile 25 arası bir sayı giriniz.")
            if (tahmin == sayi):
                print(" 🏆 Tebrikler 3.Seviyeye geçtiniz.")
                level = 3
            else:
                hak = hak-1
                if (tahmin > sayi):
                    print("Tahminin Sayıdan Daha Büyük")
                else:
                    print("Tahminin Sayıdan Daha Küçük")
        puan = puan + (hak * (level-1)) * 10
        if (hak == 0 ):
            cls = lambda: print('\n' * 100)
            cls()
            print("✘ Maalesef tahmin hakkın bitti ✘","\n✔ Doğru Cevap ≡≡⫸",sayi,"\nOyunu kaybettin",ad,"\n🏆 Kazandığın toplam puan ≡≡⫸ ",puan)
            level = 0

    if (level == 3):
        print(" ★✫✭ 3. Seviye || 1-30 Arasında bir Sayı")
        sayi = random.randint(1,30)
        hak = 6
        while(hak > 0) and (level == 3):
            print(" ❤ Kalan Hak ❤ =  ",hak)
            tahmin = 0
            while (0 >= tahmin or tahmin >= 31):
                tahmin = int(input("Tahmininizi Giriniz = "))
                if (0 >= tahmin or tahmin >= 31):
                    print("Lütfen 1 ile 30 arası bir sayı giriniz.")
            if (tahmin == sayi):
                print(" 🏆 Tebrikler 4.Seviyeye geçtiniz.")
                level = 4
            else:
                hak = hak-1
                if (tahmin > sayi):
                    print("Tahminin Sayıdan Daha Büyük")
                else:
                    print("Tahminin Sayıdan Daha Küçük")
        puan = puan + (hak * (level-1)) * 10
        if (hak == 0 ):
            cls = lambda: print('\n' * 100)
            cls()
            print("✘ Maalesef tahmin hakkın bitti ✘","\n✔ Doğru Cevap ≡≡⫸",sayi,"\nOyunu kaybettin",ad,"\n🏆 Kazandığın toplam puan ≡≡⫸ ",puan)
            level = 0

    if (level == 4):
        print(" ★✫✭✯ 4. Seviye || 1-40 Arasında bir Sayı")
        sayi = random.randint(1,40)
        hak = 5
        while(hak > 0) and (level == 4):
            print(" ❤ Kalan Hak ❤ =  ",hak)
            tahmin = 0
            while (0 >= tahmin or tahmin >= 41):
                tahmin = int(input("Tahmininizi Giriniz = "))
                if (0 >= tahmin or tahmin >= 41):
                    print("Lütfen 1 ile 40 arası bir sayı giriniz.")
            if (tahmin == sayi):
                print(" 🏆 Tebrikler 5.Seviyeye geçtiniz.")
                level = 5
            else:
                hak = hak-1
                if (tahmin > sayi):
                    print("Tahminin Sayıdan Daha Büyük")
                else:
                    print("Tahminin Sayıdan Daha Küçük")
        puan = puan + (hak * (level-1)) * 10
        if (hak == 0 ):
            cls = lambda: print('\n' * 100)
            cls()
            print("✘ Maalesef tahmin hakkın bitti ✘","\n✔ Doğru Cevap ≡≡⫸",sayi,"\nOyunu kaybettin",ad,"\n🏆 Kazandığın toplam puan ≡≡⫸ ",puan)
            level = 0

    if (level == 5):
        print(" ★✫✭✯✰ 5. Seviye || 1-50 Arasında bir Sayı")
        sayi = random.randint(1,50)
        hak = 3
        while(hak > 0) and (level == 5):
            print(" ❤ Kalan Hak ❤ =  ",hak)
            tahmin = 0
            while (0 >= tahmin or tahmin >= 51):
                tahmin = int(input("Tahmininizi Giriniz = "))
                if (0 >= tahmin or tahmin >= 51):
                    print("Lütfen 1 ile 50 arası bir sayı giriniz.")
            if (tahmin == sayi):
                puan = puan + ((hak * level)* 10)
                print(" 🎆 🎆 Tebrikler oyunu bitirdin 🎆 🎆",ad," 🎆 🎆 Sen bir ustasın. 🎆 🎆 ")
                level = 0
            else:
                hak = hak-1
                if (tahmin > sayi):
                    print("Tahminin Sayıdan Daha Büyük")
                else:
                    print("Tahminin Sayıdan Daha Küçük")
        puan = puan + (hak * level) * 10
        if (hak == 0 ):
            cls = lambda: print('\n' * 100)
            cls()
            print("✘ Maalesef tahmin hakkın bitti ✘","\n✔ Doğru Cevap ≡≡⫸",sayi,"\nOyunu kaybettin",ad,"\n🏆 Kazandığın toplam puan ≡≡⫸ ",puan)
            level = 0

    if ( level == 0 ):
        restart = input("oyunu tekrar oynamak istersen ┆Ε┆vet, eğer oynamak istemiyorsan ┆Η┆ayır =>  ")
        if (restart == "h" or restart == "H" or restart == "hayır" or restart == "Hayır"):
            print("Oyunu oynadığın için teşekkür ederim. Daha sonra görüşmek dileğiyle. :☽")
        else:
            cls = lambda: print('\n' * 100)
            cls()
            print("♔ Hadi o zaman bir daha başlayalım ♔")