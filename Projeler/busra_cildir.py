print("Kolay seviye için 1 yazın")
print("Orta seviye 2 yazın")
print("Zor seviye 3 yazın")

yeni = "n"
while yeni == "n":
    a = int(input("Zorluk seviyesini seçiniz:"))
    if a == 1:
        puan = 0
        for i in range(10):
            import random

            sayi1 = random.randint(1, 10)
            sayi2 = random.randint(1, 10)
            islemler = ["+", "-"]
            islem = random.choice(islemler)

            if islem == "+":
                sonuc = sayi1 + sayi2
                cevap = int(input("{}{}{}=".format(sayi1, islem, sayi2)))
                if cevap == sonuc:
                    puan += 10
                    print("Bildin, tebrikler!")
                else:
                    print("Bilemedin.")

            else:
                sonuc = sayi1 - sayi2
                cevap = int(input("{}{}{}=".format(sayi1, islem, sayi2)))
                if cevap == sonuc:
                    puan += 10
                    print("Bildin, tebrikler!")
                else:
                    print("Bilemedin.")

        print("Toplam Puan=", puan)
        yeni = input("Yeni oyuna başlamak için [n]ew'e, bitirmek için [f]inish'e basınız. :")

    elif a == 2:
        puan = 0
        for i in range(10):
            import random

            sayi1 = random.randint(10, 50)
            sayi2 = random.randint(10, 50)
            islemler = ["+", "-", "*"]
            islem = random.choice(islemler)

            if islem == "+":
                sonuc = sayi1 + sayi2
                cevap = int(input("{}{}{}=".format(sayi1, islem, sayi2)))
                if cevap == sonuc:
                    puan += 10
                    print("Bildin, tebrikler!")
                else:
                    print("Bilemedin.")

            elif islem == "-":
                sonuc = sayi1 - sayi2
                cevap = int(input("{}{}{}=".format(sayi1, islem, sayi2)))
                if cevap == sonuc:
                    puan += 10
                    print("Bildin, tebrikler!")
                else:
                    print("Bilemedin.")

            else:
                sonuc = sayi1 * sayi2
                cevap = int(input("{}{}{}=".format(sayi1, islem, sayi2)))
                if cevap == sonuc:
                    puan += 10
                    print("Bildin, tebrikler!")
                else:
                    print("Bilemedin.")

        print("Toplam Puan=", puan)
        yeni = input("Yeni oyuna başlamak için [n]ew'e, bitirmek için [f]inish'e basınız. :")

    elif a == 3:
        puan = 0
        for i in range(10):
            import random

            sayi1 = random.randint(50, 100)
            sayi2 = random.randint(50, 100)
            islemler = ["+", "-", "*", "/"]
            islem = random.choice(islemler)

            if islem == "+":
                sonuc = sayi1 + sayi2
                cevap = int(input("{}{}{}=".format(sayi1, islem, sayi2)))
                if cevap == sonuc:
                    puan += 10
                    print("Bildin, tebrikler!")
                else:
                    print("Bilemedin.")

            elif islem == "-":
                sonuc = sayi1 - sayi2
                cevap = int(input("{}{}{}=".format(sayi1, islem, sayi2)))
                if cevap == sonuc:
                    puan += 10
                    print("Bildin, tebrikler!")
                else:
                    print("Bilemedin.")

            elif islem == "*":
                sonuc = sayi1 * sayi2
                cevap = int(input("{}{}{}=".format(sayi1, islem, sayi2)))
                if cevap == sonuc:
                    puan += 10
                    print("Bildin, tebrikler!")
                else:
                    print("Bilemedin.")

            else:
                sonuc = sayi1 / sayi2
                sonuc = round(sonuc, 2)
                print("Bölme işlemi sonucunu virgülden sonra iki basamak şeklinde yazınız.")
                cevap = float(input("{}{}{}=".format(sayi1, islem, sayi2)))
                if cevap == sonuc:
                    puan += 10
                    print("Bildin, tebrikler!")
                else:
                    print("Bilemedin.")

        print("Toplam Puan=", puan)
        yeni = input("Yeni oyuna başlamak için [n]ew'e, bitirmek için [f]inish'e basınız. :")