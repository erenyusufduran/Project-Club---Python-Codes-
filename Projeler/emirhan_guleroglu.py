import random

print(
    "Islem oyununa hosgeldiniz. Eger 50 puan yapmayi basarabilirsen kazanirsin ama unutma ki sadece 3 hata hakkin var")
print("1. Derece zorluk = 0-10 sayilarini barindirir ve +, -, islemleri vardir.\n"
      "2. Derece zorluk = 0-50 sayilarini barindirir ve +, -, / islmeleri vardir.\n"
      "3. Derece zorluk = 0-100 sayilarini barindirir ve +, -, /, X islemleri vardir")
derece = int(input("Lutfen oynamak istediginiz dereceyi secin(1, 2 yada 3):\t"))
hata_hakki = 3
oyuncu_puani = 0
derece_1_sayilari = [*range(11)]
derece_1_islemleri = ["+", "-"]
derece_2_sayilari = [*range(51)]
derece_2_islemleri = ["+", "-", "/"]
derece_3_sayilari = [*range(101)]
derece_3_islemleri = ["+", "-", "/", "*"]
while hata_hakki > 0 or oyuncu_puani < 30:
    if derece == 1:
        sayi1 = random.choice(derece_1_sayilari)
        sayi2 = random.choice(derece_1_sayilari)
        islem = random.choice(derece_1_islemleri)
        soru = int(input("Lutfen {}{}{} isleminin cevabini giriniz:\t".format(sayi1, islem, sayi2)))
        if islem == derece_1_islemleri[0]:
            cevap = sayi1 + sayi2
            if soru == cevap:
                oyuncu_puani += 10
                print("Tebrikler cevabiniz dogru. Suan %d puaniniz var." % (oyuncu_puani))
            else:
                hata_hakki -= 1
                print("Malesef cevabiniz yanlis. Dogru cevap %d olmaliydi ve %d hata hakkiniz kaldi" % (
                cevap, hata_hakki))
        elif islem == derece_1_islemleri[1]:
            cevap = sayi1 - sayi2
            if soru == cevap:
                oyuncu_puani += 10
                print("Tebrikler cevabiniz dogru. Suan %d puaniniz var." % (oyuncu_puani))
            else:
                hata_hakki -= 1
                print("Malesef cevabiniz yanlis. Dogru cevap %d olmaliydi ve %d hata hakkiniz kaldi" % (
                cevap, hata_hakki))

    elif derece == 2:
        sayi1 = random.choice(derece_2_sayilari)
        sayi2 = random.choice(derece_2_sayilari)
        islem = random.choice(derece_2_islemleri)
        soru = int(input("Lutfen {}{}{} isleminin cevabini giriniz:\t".format(sayi1, islem, sayi2)))
        if islem == derece_2_islemleri[0]:
            cevap = sayi1 + sayi2
            if soru == cevap:
                oyuncu_puani += 10
                print("Tebrikler cevabiniz dogru. Suan %d puaniniz var." % (oyuncu_puani))
            else:
                hata_hakki -= 1
                print("Malesef cevabiniz yanlis. Dogru cevap %d olmaliydi ve %d hata hakkiniz kaldi" % (
                cevap, hata_hakki))
        elif islem == derece_2_islemleri[1]:
            cevap = sayi1 - sayi2
            if soru == cevap:
                oyuncu_puani += 10
                print("Tebrikler cevabiniz dogru. suan %d puaniniz var." % (oyuncu_puani))
            else:
                hata_hakki -= 1
                print("Malesef cevabiniz yanlis. Dogru cevap %d olmaliydi ve %d hata hakkiniz kaldi" % (
                cevap, hata_hakki))
        elif islem == derece_2_islemleri[2]:
            cevap = sayi1 // sayi2
            if soru == cevap:
                oyuncu_puani += 10
                print("Tebrikler cevabiniz dogru. Suan %d puaniniz var." % (oyuncu_puani))
            else:
                hata_hakki -= 1
                print("Malesef cevabiniz yanlis. Dogru cevap %d olmaliydi ve %d hata hakkiniz kaldi" % (
                cevap, hata_hakki))

    elif derece == 3:
        sayi1 = random.choice(derece_3_sayilari)
        sayi2 = random.choice(derece_3_sayilari)
        islem = random.choice(derece_3_islemleri)
        soru = int(input("Lutfen {}{}{} isleminin cevabini giriniz:\t".format(sayi1, islem, sayi2)))
        if islem == derece_3_islemleri[0]:
            cevap = sayi1 + sayi2
            if soru == cevap:
                oyuncu_puani += 10
                print("Tebrikler cevabiniz dogru. Suan %d puaniniz var." % (oyuncu_puani))
            else:
                hata_hakki -= 1
                print("Malesef cevabiniz yanlis. Dogru cevap %d olmaliydi ve %d hata hakkiniz kaldi" % (
                cevap, hata_hakki))
        elif islem == derece_3_islemleri[1]:
            cevap = sayi1 - sayi2
            if soru == cevap:
                oyuncu_puani += 10
                print("Tebrikler cevabiniz dogru. Suan %d puaniniz var." % (oyuncu_puani))
            else:
                hata_hakki -= 1
                print("Malesef cevabiniz yanlis. Dogru cevap %d olmaliydi ve %d hata hakkiniz kaldi" % (
                cevap, hata_hakki))
        elif islem == derece_3_islemleri[2]:
            cevap == sayi1 // sayi2
            if soru == cevap:
                oyuncu_puani += 10
                print("Tebrikler cevabiniz dogru. Suan %d puaniniz var." % (oyuncu_puani))
            else:
                hata_hakki -= 1
                print("Malesef cevabiniz yanlis. Dogru cevap %d olmaliydi ve %d hata hakkiniz kaldi" % (
                cevap, hata_hakki))
        elif islem == derece_3_islemleri[3]:
            cevap == sayi1 * sayi2
            if soru == cevap:
                oyuncu_puani += 10
                print("Tebrikler cevabiniz dogru. Suan %d puaniniz var." % (oyuncu_puani))
            else:
                hata_hakki -= 1
                print("Malesef cevabiniz yanlis. Dogru cevap %d olmaliydi ve %d hata hakkiniz kaldi" % (
                cevap, hata_hakki))
    else:
        print("Lutfen 1., 2. yada 3. derecelerden birini seciniz")

    if oyuncu_puani == 30 or hata_hakki == 0:
        if oyuncu_puani == 30:
            tekrar = input("Tebrikler oyunu kazandiniz. Peki tekrar oynamak istermisiniz(E yada H) ?:\t").upper()
            if tekrar == "E":
                oyuncu_puani = 0
            else:
                break
        elif hata_hakki == 0:
            tekrar = input("Malesef oyunu kazanamadiniz. Peki tekrar oynamak istermisiniz(E yada H) ?:\t").upper()
            if tekrar == "E":
                hata_hakki = 3
            else:
                break