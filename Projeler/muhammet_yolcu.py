import random

print("Matematik oyunumuza hoşgeldiniz. Bu oyunda amacımız matematiğinizi sınayarak geliştirmek.")
print(
    "Oyunumuzda en basit seviyeden başlayarak , aldığınız puanlarla seviye atlayıp bir sonraki seviyeye geçebilirsiniz.")
print("Soruları doğru yanıtlayarak topladığınız her 100 puanda diğer seviyeye geçersiniz.")
print("Her aşama için 3 yanlış cevap hakkınız bulunmaktadır.")
print("Oyun başlıyor... Başarılar.")
aşama = 1

while aşama < 5:

    print("{} . aşamaya hoşgeldiniz. Oyunumuz başlıyor..".format(aşama))

    while aşama == 1:
        hak = 2
        puan = 0
        soru = 1
        print("1. aşamada sadece toplama ve çıkarma işlemleri sorulacaktır.")

        while True:
            sayı1 = random.randint(1, 20)
            sayı2 = random.randint(1, 20)

            toplama = sayı1 + sayı2
            çıkarma = sayı1 - sayı2
            işlem = ["+", "-"]
            a = random.choice(işlem)
            print("{} . soru ".format(soru))
            print("{}{}{}= ? işleminin cevabı nedir ?".format(sayı1, a, sayı2))
            cevap = int(input())

            if cevap == toplama and a == işlem[0]:
                print(" Tebrikler doğru bildiniz. 10 puan.")
                puan += 10
                print(" Toplam puanınız : {} ".format(puan))


            elif cevap == çıkarma and a == işlem[1]:
                print(" Tebrikler doğru bildiniz. 10 puan.")
                puan += 10
                print(" Toplam puanınız : {} ".format(puan))

            elif a == işlem[0]:

                print("Yanlış cevap verdiniz. Doğru cevap = {}".format(toplama))

                print("{} hata hakkınız kaldı".format(hak))

                hak -= 1
            else:

                print("Yanlış cevap verdiniz. Doğru cevap = {}".format(çıkarma))
                print("{} hata hakkınız kaldı".format(hak))
                hak -= 1

            if hak < 0:
                print("Hiç hakkınız kalmamıştır. Oyun bitti. Lütfen tekrar deneyin")
                aşama -= 1
                break
            if puan == 100:
                aşama += 1
                print("Tebrikler.{} . seviyeye geçmeye hak kazandınız".format(aşama))
                break
            soru += 1
        break

    while aşama == 2:
        hak = 2
        puan = 0
        soru = 1
        print("Tebrikler 2. aşamaya geçtiniz. 2. aşamada toplama,çıkarma ve çarpma işlemleri sorulacaktır.")

        while True:
            sayı1 = random.randint(1, 40)
            sayı2 = random.randint(2, 10)

            toplama = sayı1 + sayı2
            çıkarma = sayı1 - sayı2
            çarpma = sayı1 * sayı2
            işlem = ["+", "-", "*"]
            a = random.choice(işlem)
            print("{} . soru ".format(soru))
            print("{}{}{}= ? işleminin cevabı nedir ?".format(sayı1, a, sayı2))
            cevap = int(input())

            if cevap == toplama and a == işlem[0]:
                print("Tebrikler doğru bildiniz.. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))


            elif cevap == çıkarma and a == işlem[1]:
                print("Tebrikler doğru bildiniz... 10 puan.")
                puan += 10
                print("Toplam puanınız : {}".format(puan))
            elif cevap == çarpma and a == işlem[2]:
                print("Tebrikler doğru bildiniz...  10 puan")
                puan += 10
                print("Toplam puanınız : {} ".format(puan))

            elif a == işlem[0]:
                print("Yanlış cevap verdiniz. Doğru cevap = {}".format(toplama))
                print("{} hata hakkınız kaldı".format(hak))

                hak -= 1
            elif a == işlem[1]:
                print("Yanlış cevap verdiniz. Doğru cevap = {}".format(çıkarma))
                print("{} hata hakkınız kaldı".format(hak))

                hak -= 1
            else:
                print("Yanlış cevap verdiniz. Doğru cevap = {}".format(çarpma))
                print("{} hata hakkınız kaldı".format(hak))

                hak -= 1
            if hak < 0:
                print("Hiç hakkınız kalmamıştır. Oyun bitti. Lütfen tekrar deneyin")
                aşama -= 1
                break
            if puan == 100:
                aşama += 1
                print("Tebrikler.{} . seviyeye geçmeye hak kazandınız".format(aşama))
                break
            soru += 1
        break
    while aşama == 3:
        hak = 2
        puan = 0
        soru = 1
        print("Tebrikler 3. aşamaya geçtiniz. 3. aşamada toplama,çıkarma, çarpma ve bölme işlemleri sorulacaktır.")
        print("Bölme işlemlerinde sadece tam sayıyı yazmanız yeterlidir.")
        while True:
            sayı1 = random.randint(20, 100)
            sayı2 = random.randint(2, 20)

            toplama = sayı1 + sayı2
            çıkarma = sayı1 - sayı2
            çarpma = sayı1 * sayı2
            bölme = sayı1 // sayı2
            işlem = ["+", "-", "*", "/"]
            a = random.choice(işlem)
            print("{} . soru ".format(soru))
            print("{}{}{}= ? işleminin cevabı nedir ?".format(sayı1, a, sayı2))
            cevap = int(input())

            if cevap == toplama and a == işlem[0]:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))


            elif cevap == çıkarma and a == işlem[1]:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan += 10
                print("Toplam puanınız : {}".format(puan))
            elif cevap == çarpma and a == işlem[2]:
                print("Tebrikler doğru bildiniz...  10 puan")
                puan += 10
                print("Toplam puanınız : {} ".format(puan))

            elif cevap == bölme and a == işlem[3]:
                print("Tebrikler doğru bildiniz...  10 puan")
                puan += 10
                print("Toplam puanınız : {} ".format(puan))

            elif a == işlem[0]:
                print("Yanlış cevap verdiniz. Doğru cevap = {}".format(toplama))
                print("{} hata hakkınız kaldı".format(hak))

                hak -= 1
            elif a == işlem[1]:
                print("Yanlış cevap verdiniz. Doğru cevap = {}".format(çıkarma))
                print("{} hata hakkınız kaldı".format(hak))

                hak -= 1
            elif a == işlem[2]:
                print("Yanlış cevap verdiniz. Doğru cevap = {}".format(çarpma))
                print("{} hata hakkınız kaldı".format(hak))

                hak -= 1
            else:
                print("Yanlış cevap verdiniz. Doğru cevap = {}".format(bölme))
                print("{} hata hakkınız kaldı".format(hak))

                hak -= 1
            if hak < 0:
                print("Hiç hakkınız kalmamıştır. Oyun bitti. Lütfen tekrar deneyin")
                aşama -= 1
                break
            if puan == 100:
                aşama += 1
                print("Tebrikler.{} . seviyeye geçmeye hak kazandınız".format(aşama))
                break
            soru += 1
        break
    while aşama == 4:
        hak = 2
        puan = 0
        soru = 1
        print("Tebrikler 4. ve son aşamaya geçmeye hak kazandınız")
        print("Bu aşamada artık 4 işleminde bir arada kullanıldığı sorularla karşılaşacağız.")
        print("Bilmeyenler için 4 işlemde , işlem önceliği sırasını hatırlatalım.")
        print("Çarpma > Bölme > Toplama = Çıkarma")

        while True:

            sayı1 = random.randint(2, 50)
            sayı2 = random.randint(2, 50)
            sayı3 = random.randint(50, 200)
            sayı4 = random.randint(2, 30)

            işlem_1 = (sayı1 - sayı2) + (sayı3 // sayı4)
            işlem_2 = (sayı1 - sayı2) + (sayı1 * sayı2)
            işlem_3 = (sayı1 - sayı2) + (sayı1 - sayı2)
            işlem_4 = (sayı3 // sayı4) + (sayı1 * sayı2)
            işlem_5 = (sayı3 // sayı4) + (sayı3 // sayı4)
            işlem_6 = (sayı1 * sayı2) + (sayı1 * sayı2)

            a = "+"
            b = "-"
            c = "*"
            d = "/"
            soru1 = (str(sayı3) + d + str(sayı4))
            soru2 = (str(sayı1) + b + str(sayı2))
            soru3 = (str(sayı1) + c + str(sayı2))
            sorular = [soru1, soru2, soru3]
            x = random.choice(sorular)
            y = random.choice(sorular)

            print("{} . soru ".format(soru))
            print("{}{}{}= ? işleminin cevabı nedir ?".format(x, a, y))
            cevap = int(input())

            if cevap == işlem_1 and x == soru2 and y == soru1:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))
            elif cevap == işlem_2 and x == soru2 and y == soru3:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))
            elif cevap == işlem_3 and x == soru2 and y == soru2:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))
            elif cevap == işlem_1 and x == soru1 and y == soru2:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))
            elif cevap == işlem_4 and x == soru1 and y == soru3:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))
            elif cevap == işlem_5 and x == soru1 and y == soru1:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))
            elif cevap == işlem_2 and x == soru3 and y == soru2:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))
            elif cevap == işlem_4 and x == soru3 and y == soru1:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))
            elif cevap == işlem_6 and x == soru3 and y == soru3:
                print("Tebrikler doğru bildiniz. 10 puan.")
                puan = puan + 10
                print("Toplam puanınız : {} ".format(puan))



            else:
                print("Yanlış cevap verdiniz")
                print("{} hata hakkınız kaldı".format(hak))

                hak -= 1
            if puan == 100:
                aşama += 1
                break
            if hak < 0:
                print("Hiç hakkınız kalmamıştır. Oyun bitti. Lütfen tekrar deneyin")
                aşama -= 1
                break

            soru += 1
        break
    break

if aşama == 5:
    print("Tebrikler oyunumuzu başarıyla tamamladınız.")
    print("Sonraki sürümler için beklemede kalın :))))")