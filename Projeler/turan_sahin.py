# Kütüphaneler
import random

# Değişkenler
arti = "+"
eksi = "-"
carpma = "x"
bolme = ":"
esittir = "="
devam = "E"
dogru = 0
yanlıs = 0

# Açıklama
print("""
      İşlem oyununa hoşgeldiniz. Bu oyunda size verilen işlemin sonucunu
      bulmanız gerekiyor.
      """)
while devam == "E":

    # Sorular
    # Zorluk seviyesi belirleme
    zorluk = "x"
    zorluk = input("Lütfen zorluk seviyesi belirleyin: [K]OLAY / [O]RTA / [Z]OR:")

    # Soruların oluşturulması ve cevaplanması

    # Kolay
    if zorluk == "K":
        sayi1 = str(random.randint(1, 20))
        sayi2 = str(random.randint(1, 20))
        islem = random.randint(0, 1)

        # Kolay toplama
        if islem == 0:
            islemArti = sayi1 + arti + sayi2 + esittir
            sonucArti = int(input(islemArti))
            if sonucArti == int(sayi1) + int(sayi2):
                print("Tebrikler, bildin!!")
                dogru += 1
            else:
                print("Üzgünüm bilemedin.")
                yanlıs += 1

        # Kolay çıkarma
        else:
            islemEksi = sayi1 + eksi + sayi2 + esittir
            sonucEksi = int(input(islemEksi))
            if sonucEksi == int(sayi1) - int(sayi2):
                print("Tebrikler, bildin!!")
                dogru += 1
            else:
                print("Üzgünüm, bilemedin.")
                yanlıs += 1

    # Orta
    elif zorluk == "O":
        sayi1 = str(random.randint(1, 50))
        sayi2 = str(random.randint(1, 50))
        islem = random.randint(0, 2)

        # Toplama orta
        if islem == 0:
            islemArti = sayi1 + arti + sayi2 + esittir
            sonucArti = int(input(islemArti))
            if sonucArti == int(sayi1) + int(sayi2):
                print("Tebrikler bildin!!")
                dogru += 1
            else:
                print("Üzgünüm bilemedin.")
                yanlıs += 1

        # Çıkarma orta
        elif islem == 1:
            islemEksi = sayi1 + eksi + sayi2 + esittir
            sonucEksi = int(input(islemEksi))
            if sonucEksi == int(sayi1) - int(sayi2):
                print("Tebrikler, bildin!!")
                dogru += 1
            else:
                print("Üzgünüm, bilemedin.")
                yanlıs += 1

        # Çarpma orta
        else:
            islemCarpma = sayi1 + carpma + sayi2 + esittir
            sonucCarpma = int(input(islemCarpma))
            if sonucCarpma == int(sayi1) * int(sayi2):
                print("Tebrikler, bildin!!")
                dogru += 1
            else:
                print("Üzgünüm, bilemedin.")
                yanlıs += 1

    # Zor
    else:
        sayi1 = str(random.randint(10, 150))
        sayi2 = str(random.randint(10, 150))
        islem = random.randint(0, 3)

        # Toplama zor
        if islem == 0:
            islemArti = sayi1 + arti + sayi2 + esittir
            sonucArti = int(input(islemArti))
            if sonucArti == int(sayi1) + int(sayi2):
                print("Tebrikler bildin!!")
                dogru += 1
            else:
                print("Üzgünüm bilemedin.")
                yanlıs += 1

        # Çıkarma zor
        elif islem == 1:
            islemEksi = sayi1 + eksi + sayi2 + esittir
            sonucEksi = int(input(islemEksi))
            if sonucEksi == int(sayi1) - int(sayi2):
                print("Tebrikler, bildin!!")
                dogru += 1
            else:
                print("Üzgünüm, bilemedin.")
                yanlıs += 1

        # Çarpma zor
        elif islem == 2:
            islemCarpma = sayi1 + carpma + sayi2 + esittir
            sonucCarpma = int(input(islemCarpma))
            if sonucCarpma == int(sayi1) * int(sayi2):
                print("Tebrikler, bildin!!")
                dogru += 1
            else:
                print("Üzgünüm, bilemedin.")
                yanlıs += 1

        # Bölme zor
        else:
            islemBolme = sayi1 + bolme + sayi2 + esittir
            sonucBolme = int(input(islemBolme))
            if sonucBolme == int(sayi1) / int(sayi2):
                print("Tebrikler, bildin!!")
                dogru += 1
            else:
                print("Üzgünüm, bilemedin.")
                yanlıs += 1

    # Skorboard
    Skorboard = "Skorunuz —> Doğru:{} Yanlış:{}".format(dogru, yanlıs)
    print(Skorboard)

    # Tamam mı devam mı?
    devam = input("Devam etmek istiyor musunuz? [E]vet / [H]ayır:")

# Veda
print("Oyunumuzu oynadığın için teşekkürler. Hoşçakal!!")