print("Matematik oyununa hoşgeldiniz.")
print("a.Kendini test et")
print("b.Sonsuz")
print("c.Zamanla yarış")
mod = input("Oynamak istediğiniz oyun modunu seçiniz.[a]/[b]/[c]=")

if mod == "a":
    print(" ")
    print("Bu oyun modu 10 sorudan oluşur.")
    print(" ")
    print("a.Kolay (Sayı aralığı(0-10)) (Sadece toplama işlemini içerir.)")
    print(
        "b.Orta (Sayı aralığı(0-50)) (Toplama ve çıkarma işlemlerini içerir.)")
    print(
        "c.Zor (Sayı aralığı(0-100)) (Toplama, çıkarma, bölme ve çarpma işlemlerini içerir)"
    )
    zor = input("Oyun zorluğunu seçiniz. [a]/[b]/[c]=")

    if zor == "a":
        import time

        time.sleep(1)
        print('\033c')
        print('\x1bc')
        sayac = 0
        dogru = 0
        yanlis = 0
        while sayac < 10:
            import random

            sayi1 = random.randint(0, 10)
            sayi2 = random.randint(0, 10)
            ac = sayi1 + sayi2
            print(sayi1, "+", sayi2, "=?")
            cev = int(input("Cevap="))
            sayac += 1
            if cev == ac:
                dogru += 1
            else:
                yanlis += 1
        print("10 sorunun içinde:")
        print("Doğru sayısı=", dogru, " Yanlış sayısı=", yanlis)

    elif zor == "b":
        import time

        time.sleep(1)
        print('\033c')
        print('\x1bc')
        sayac = 0
        dogru = 0
        yanlis = 0
        while sayac < 10:
            import random

            sayi1 = random.randint(0, 50)
            sayi2 = random.randint(0, 50)
            sym = random.choice(['+', '-'])
            if sym == '+':
                ac = sayi1 + sayi2
                print(sayi1, sym, sayi2, "=?")
                cev = int(input("Cevap="))
            elif sym == '-':
                if sayi1 > sayi2:
                    ac = sayi1 - sayi2
                    print(sayi1, sym, sayi2, "=?")
                    cev = int(input("Cevap="))
                else:
                    ac = sayi2 - sayi1
                    print(sayi2, sym, sayi1, "=?")
                    cev = int(input("Cevap="))

            sayac += 1
            if cev == ac:
                dogru += 1
            else:
                yanlis += 1
        print("10 sayının içinde")
        print("Doğru sayısı=", dogru, " Yanlış sayısı=", yanlis)

    elif zor == "c":
        print(" ")
        print(
            "Bölme işleminde tam bölünen sayılar gelmez ise, lütfen sadece virgülden önceki kısmını yazınız"
        )
        print(" ")
        input("Başlamak için herhangi bir tuşa basın")
        import time

        time.sleep(1)
        print('\033c')
        print('\x1bc')
        sayac = 0
        dogru = 0
        yanlis = 0

        while sayac < 10:
            import random

            sayi1 = random.randint(0, 100)
            sayi2 = random.randint(0, 100)
            sym = random.choice(['+', '-', '*', '//'])
            if sym == '+':
                ac = sayi1 + sayi2
                print(sayi1, sym, sayi2, "=?")
                cev = int(input("Cevap="))
            elif sym == '*':
                ac = sayi1 * sayi2
                print(sayi1, sym, sayi2, "=?")
                cev = int(input("Cevap="))
            elif sym == '//':
                if sayi1 > sayi2:
                    ac = sayi1 // sayi2
                    print(sayi1, sym, sayi2, "=?")
                    cev = int(input("Cevap="))
                else:
                    ac = sayi2 // sayi1
                    print(sayi2, sym, sayi1, "=?")
                    cev = int(input("Cevap="))
            else:
                if sayi1 > sayi2:
                    ac = sayi1 - sayi2
                    print(sayi1, sym, sayi2, "=?")
                    cev = int(input("Cevap="))

                else:
                    ac = sayi2 - sayi1
                    print(sayi2, sym, sayi1, "=?")
                    cev = int(input("Cevap="))

            sayac += 1
            if cev == ac:
                dogru += 1
            else:
                yanlis += 1

        print("10 sayının içinde")
        print("Doğru sayısı=", dogru, " Yanlış sayısı=", yanlis)

elif mod == "b":
    print(" ")
    print(
        "Bu oyun modunda amaç hiç yanlış yapmadan ilerleyebildiğiniz kadar ilerlemektir. Dört işlemi ve 1-100'e kadar olan sayıları içerir."
    )
    print(" ")
    print(
        "Bölme işleminde tam bölünen sayılar gelmez ise, lütfen sadece virgülden önceki kısmını yazınız"
    )
    print(" ")
    input("Başlamak için enter tuşuna basın")
    import time

    time.sleep(1)
    print('\033c')
    print('\x1bc')
    sayac = True
    skor = 0

    while sayac == True:
        import random

        sayi1 = random.randint(0, 100)
        sayi2 = random.randint(0, 100)
        sym = random.choice(['+', '-', '*', '//'])

        if sym == '+':
            ac = sayi1 + sayi2
            print(sayi1, sym, sayi2, "=?")
            cev = int(input("Cevap="))
        elif sym == '*':
            ac = sayi1 * sayi2
            print(sayi1, sym, sayi2, "=?")
            cev = int(input("Cevap="))
        elif sym == '//':
            if sayi1 > sayi2:
                ac = sayi1 // sayi2
                print(sayi1, sym, sayi2, "=?")
                cev = int(input("Cevap="))
            else:
                ac = sayi2 // sayi1
                print(sayi2, sym, sayi1, "=?")
                cev = int(input("Cevap="))
        else:
            if sayi1 > sayi2:
                ac = sayi1 - sayi2
                print(sayi1, sym, sayi2, "=?")
                cev = int(input("Cevap="))

            else:
                ac = sayi2 - sayi1
                print(sayi2, sym, sayi1, "=?")
                cev = int(input("Cevap="))

        if cev == ac:
            print("Doğru!")
            skor += 1
        else:
            print("Yanlış")
            print("Skor=", skor)
            t = input("Tekrar denemek ister misin? [e]vet / [h]ayır=")
            if t == "e":
                skor = 0
                print('\033c')
                print('\x1bc')
                sayac = True
            else:
                print('\033c')
                print('\x1bc')
                sayac = False

elif mod == "c":
    print("")
    print(
        "Bu oyun modunda amacınız 30 saniye boyunca yapabildiğiniz kadar soruyu doğru cevaplamaktır. Yanlış yapmanızın önemi yoktur,skora etki etmez veya oyunun bitmesine neden olmaz."
    )
    print("")
    input("Başlamak için [enter]e basınız.")
    print('\033c')
    print('\x1bc')
    import time

    time.sleep(1)
    time_limit = 30
    start_time = time.time()
    # print(start_time)
    skor = 0
    while True:
        elapsed_time = time.time() - start_time
        print(" ")
        print("Kalan süreniz=", time_limit - int(elapsed_time), "saniye")
        print(" ")
        if time_limit > elapsed_time:
            import random

            sayi1 = random.randint(1, 100)
            sayi2 = random.randint(1, 100)
            sym = random.choice(['+', '-', '*', '//'])

            if sym == '+':
                ac = sayi1 + sayi2
                print(sayi1, sym, sayi2, "=?")
                cev = int(input("Cevap="))
                if cev == ac:
                    print("Doğru!")
                    skor += 1
                else:
                    print("Yanlış!")
                    skor = skor

            elif sym == '*':
                ac = sayi1 * sayi2
                print(sayi1, sym, sayi2, "=?")
                cev = int(input("Cevap="))
                if cev == ac:
                    print("Doğru!")
                    skor += 1
                else:
                    print("Yanlış!")
                    skor = skor

            elif sym == '//':
                if sayi1 > sayi2:
                    ac = sayi1 // sayi2
                    print(sayi1, sym, sayi2, "=?")
                    cev = int(input("Cevap="))
                    if cev == ac:
                        print("Doğru!")
                        skor += 1
                    else:
                        print("Yanlış!")
                        skor = skor

                else:
                    ac = sayi2 // sayi1
                    print(sayi2, sym, sayi1, "=?")
                    cev = int(input("Cevap="))
                    if cev == ac:
                        print("Doğru!")
                        skor += 1
                    else:
                        print("Yanlış!")
                        skor = skor

            else:
                if sayi1 > sayi2:
                    ac = sayi1 - sayi2
                    print(sayi1, sym, sayi2, "=?")
                    cev = int(input("Cevap="))
                    if cev == ac:
                        print("Doğru!")
                        skor += 1
                    else:
                        print("Yanlış!")
                        skor = skor

                else:
                    ac = sayi2 - sayi1
                    print(sayi2, sym, sayi1, "=?")
                    cev = int(input("Cevap="))
                    if cev == ac:
                        print("Doğru!")
                        skor += 1
                    else:
                        print("Yanlış!")
                        skor = skor

        elif elapsed_time > time_limit:
            print("")
            print("Süreniz doldu")
            print("30 Saniyede Yaptığınız Skor=", skor)
            print(" ")
            import time

            time.sleep(5)
            print('\033c')
            print('\x1bc')
            break