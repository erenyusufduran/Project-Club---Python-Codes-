import random

islem = input('YAPACAĞINIZ İŞLEMİ SEÇİNİZ: (1 TOPLAMA 2 ÇARPMA 3 ÇIKARMA 4 BÖLME)')
if int(islem) == 1:

    aa = input('zorluk derecesini giriniz (kolay,1 orta,2 zor,3):')
    zorluk = int(aa)
    if zorluk == 1:
        sayi1 = random.randint(1, 10)
        sayi2 = random.randint(1, 10)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 + sayi2
        print("ipucu: cevap ", sonuc)
    elif zorluk == 2:
        sayi1 = random.randint(10, 999)
        sayi2 = random.randint(10, 999)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 + sayi2
        print("ipucu: cevap ", sonuc)
    elif zorluk == 3:
        sayi1 = random.randint(100, 9999)
        sayi2 = random.randint(100, 9999)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 + sayi2
        print("ipucu: cevap ", sonuc)

    user = input("birinci ve i̇kinci sayının toplamını yazınız: ")
    print(user)

    if int(user) == sonuc:
        print("CEVAP DOĞRU")
    else:
        print("CEVAP YALNIŞ")

elif int(islem) == 2:

    aa = input('zorluk derecesini giriniz (kolay,1 orta,2 zor,3):')
    zorluk = int(aa)
    if zorluk == 1:
        sayi1 = random.randint(1, 10)
        sayi2 = random.randint(1, 10)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 * sayi2
        print("ipucu: cevap ", sonuc)
    elif zorluk == 2:
        sayi1 = random.randint(10, 999)
        sayi2 = random.randint(10, 999)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 * sayi2
        print("ipucu: cevap ", sonuc)
    elif zorluk == 3:
        sayi1 = random.randint(100, 9999)
        sayi2 = random.randint(100, 9999)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 * sayi2
        print("ipucu: cevap ", sonuc)

    user = input("birinci ve i̇kinci sayının toplamını yazınız: ")
    print(user)

    if int(user) == sonuc:
        print("CEVAP DOĞRU")
    else:
        print("CEVAP YALNIŞ")





elif int(islem) == 3:

    aa = input('zorluk derecesini giriniz (kolay,1 orta,2 zor,3):')
    zorluk = int(aa)
    if zorluk == 1:
        sayi1 = random.randint(1, 10)
        sayi2 = random.randint(1, 10)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 - sayi2
        print("ipucu: cevap ", sonuc)
    elif zorluk == 2:
        sayi1 = random.randint(10, 999)
        sayi2 = random.randint(10, 999)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 - sayi2
        print("ipucu: cevap ", sonuc)
    elif zorluk == 3:
        sayi1 = random.randint(100, 9999)
        sayi2 = random.randint(100, 9999)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 - sayi2
        print("ipucu: cevap ", sonuc)

    user = input("birinci ve i̇kinci sayının toplamını yazınız: ")
    print(user)

    if int(user) == sonuc:
        print("CEVAP DOĞRU")
    else:
        print("CEVAP YALNIŞ")




elif int(islem) == 4:

    aa = input('zorluk derecesini giriniz (kolay,1 orta,2 zor,3):')
    zorluk = int(aa)
    if zorluk == 1:
        sayi1 = random.randint(1, 10)
        sayi2 = random.randint(1, 10)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 / sayi2
        print("ipucu: cevap ", sonuc)
    elif zorluk == 2:
        sayi1 = random.randint(10, 999)
        sayi2 = random.randint(10, 999)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 / sayi2
        print("ipucu: cevap ", sonuc)
    elif zorluk == 3:
        sayi1 = random.randint(100, 9999)
        sayi2 = random.randint(100, 9999)
        print("birinci sayı: ", sayi1)
        print("i̇kinci sayı: ", sayi2)
        sonuc = sayi1 / sayi2
        print("ipucu: cevap ", sonuc)

    user = input("birinci ve i̇kinci sayının toplamını yazınız: ")
    print(user)

    if float(user) == sonuc:
        print("CEVAP DOĞRU")
    else:
        print("CEVAP YALNIŞ")
