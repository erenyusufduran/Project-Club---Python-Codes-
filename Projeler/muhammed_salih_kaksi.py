import random

print("Zorluk seviyeleri:")
print("1. seviye:Kolay(2 sayıyı(1'den 10'a kadar) toplama yada çıkarma)")
print("2. seviye:Orta(2 sayıyı(10'dan 20'ye kadar) toplama,çıkarma,çarpma veya bölme)")
print("3. seviye:Zor(2 sayıyı(30'dan 50'ye kadar)  çarpma veya bölme)")
print("4. seviye:Daha zor(2 sayıyı(70'den 120'ye kadar) çarpma veya bölme")
print("5.seviye:Çok daha zor(3 sayıyı(100'den 200'ye kadar) çarpma veya bölme")
zorluk = int(input("Seviye seçiniz(1-5):"))

hak = 10
puan = 0
cozulensoru = 0
yanlıssoru = 0
dogrusoru = 0
if zorluk == 1:
    deger1 = 1
    deger2 = 10
    islem1 = ["t", "c"]
    hak = 3
    sorupuan = 5
if zorluk == 2:
    deger1 = 10
    deger2 = 20
    islem1 = ["t", "c", "x", "b"]
    hak = 2
    sorupuan = 10
if zorluk == 3:
    deger1 = 30
    deger2 = 50
    islem1 = ["x", "b"]
    hak = 2
    sorupuan = 15
if zorluk == 4:
    deger1 = 70
    deger2 = 120
    islem1 = ["x", "b"]
    hak = 2
    sorupuan = 20
if zorluk == 5:
    deger1 = 100
    deger2 = 200
    islem1 = ["x", "b"]
    hak = 1
    sorupuan = 30

sayı1 = random.randint(deger1, deger2)
sayı2 = random.randint(deger1, deger2)
sayı3 = random.randint(deger1, deger2)
islem = random.choice(islem1)
islem2 = random.choice(islem1)

while True:
    print("")
    if cozulensoru == 0:
        print("Soru 1")
    if cozulensoru > 0:
        print("Soru", cozulensoru + 1)

    if zorluk < 5:
        if islem == "t":
            sonuc = sayı1 + sayı2
            print(sayı1, "+", sayı2)
        elif islem == "c":
            if zorluk == 1:
                if sayı1 > sayı2:
                    sonuc = sayı1 - sayı2
                    print(sayı1, "-", sayı2)
                elif sayı1 < sayı2:
                    sonuc = sayı2 - sayı1
                    print(sayı2, "-", sayı1)
            elif zorluk == 2:
                sonuc = sayı1 - sayı2
                print(sayı1, "-", sayı2)
        elif islem == "x":
            sonuc = sayı1 * sayı2
            print(sayı1, "*", sayı2)
        elif islem == "b":
            if sayı1 > sayı2:
                sonuc = sayı1 // sayı2
                print(sayı1, "/", sayı2)
            elif sayı2 > sayı1:
                sonuc = sayı2 // sayı1
                print(sayı2, "/", sayı1)

    if zorluk == 5:
        if islem == "x":
            if islem2 == "x":
                sonuc = sayı1 * sayı2 * sayı3
                print(sayı1, "*", sayı2, "*", sayı3)
            elif islem2 == "b":
                sonuc = sayı1 * sayı2 // sayı3
                print(sayı1, "*", sayı2, "/", sayı3)
        elif islem == "b":
            if islem2 == "x":
                sonuc = sayı1 / sayı2 * sayı3
                print(sayı1, "/", sayı2, "*", sayı3)
            elif islem2 == "b":
                sonuc = sayı1 // sayı2 // sayı3
                if sonuc < 1:
                    pass
                if sonuc > 1:
                    print(sayı1, "/", sayı2, "/", sayı3)

    cevap = int(input("Cevabınızı yazınız: "))
    if cevap == sonuc:
        if zorluk < 5:
            if islem == "b":
                kalan = sayı1 % sayı2
                cevap4 = int(input("Doğru cevap şimdiyse kalan kaç? "))
                if cevap4 == kalan:
                    print("----------------")
                    print("Doğru bildin!")
                    print("----------------")
                    dogrusoru += 1
                    cozulensoru += 1
                    puan += sorupuan
                    print("Kazanılan puan:", sorupuan)
                elif cevap4 != kalan:
                    print("Kalan hariç doğru...")
                    cozulensoru += 1
                    yanlıssoru += 1
                    puan -= int(sorupuan / 4)
                    print("Kaybedilen puan:", int(sorupuan / 4))
        if zorluk < 5:
            if islem != "b":
                print("----------------")
                print("Doğru bildin!")
                print("----------------")
                dogrusoru += 1
                cozulensoru += 1
                puan += sorupuan
                print("Kazanılan puan", sorupuan)
        print("Güncel puan:", puan)
        print("")
        cevap2 = input("Devam etmek ister misin? [E]vet veya [H]ayır ")
        if cevap2 == "E":
            sayı1 = random.randint(deger1, deger2)
            sayı2 = random.randint(deger1, deger2)
            sayı3 = random.randint(deger1, deger2)
            islem = random.choice(islem1)
            islem2 = random.choice(islem1)
            pass
        elif cevap2 == "H":
            print("")
            print("Görüşürüz")
            print("Puanınız:", puan)
            print("----------------")
            print("Çözdüğün soru sayısı:", cozulensoru)
            print("Cözdüğün doğru soru sayısı:", dogrusoru)
            print("Çözdüğün yanlış soru sayısı:", yanlıssoru)
            print("----------------")

            break
        else:
            print("Böyle bir şık yoktu")
            break
    else:
        hak -= 1
        if hak > 0:
            print("----------------")
            print("Bu soru için kalan hakkınız:", hak)
            print("----------------")
        if hak == 0:
            print("------------------------------")
            print("Bu soru için hakkın bitti.")
            print("------------------------------")
            print("Doğru cevap:", sonuc)
            cozulensoru += 1
            yanlıssoru += 1
            puan -= int(sorupuan / 2)
            print("Kaybedilen puan:", int(sorupuan / 2))
            print("Güncel puan:", puan)
            print("")
            cevap3 = input("Devam etmek ister misin? [E]vet veya [H]ayır ")
            if cevap3 == "E":
                sayı1 = random.randint(deger1, deger2)
                sayı2 = random.randint(deger1, deger2)
                sayı3 = random.randint(deger1, deger2)
                islem = random.choice(islem1)
                islem2 = random.choice(islem1)
                pass
            elif cevap3 == "H":
                print("")
                print("Görüşürüz")
                print("Puanınız:", puan)
                print("----------------")
                print("Çözdüğün soru sayısı:", cozulensoru)
                print("Çözdüğün doğru sayısı:", dogrusoru)
                print("Cözdüğün yanlış soru sayısı:", yanlıssoru)
                print("----------------")
                print("Puanınız:", puan)
                break
            else:
                print("Böyle bi şık yoktu...")
                break

            if zorluk == 1:
                hak = 3
            if zorluk == 2:
                hak = 2
            if zorluk == 3:
                hak = 2
            if zorluk == 4:
                hak = 2
            if zorluk == 5:
                hak = 1

quit

# Muhammed Salih Kakşi tarafından yapılmıştır.
