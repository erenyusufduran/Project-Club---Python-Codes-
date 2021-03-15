# Proje: Bilgisayarın rastgele ürettiği iki sayı ve işlemin sonucunu kullanıcıya soran bir uygulama kodlama
import random

print(
    'Furkan ARİYURT tarafından kodlanan "More More Math Application" Hoşgeldiniz! İsminizle hitap edebilmem için lütfen adınızı giriniz: ')
name = input()

print(
    "\nDört İşlem Uygulamamızın Kuralları:\n  1- Oyunumuzda 3 zorluk seviyesi vardır.\n     a)Kolay Seviye(0 puan - 20 puan)(1 ila 10 sayıları arasından)\n     b)Orta Seviye(21 puan - 40 puan)(1 ila 100 sayıları arasından)\n     c)Zor Seviye(41 puan - sonsuz puan)(1 iila 1000 sayıları arasından)\n  2- Her zorluk seviyesinde(Zor Seviye hariç(Doğru cevap 5, yanlış -1)) cevaplanan her doğru sonuç 2 puan, yanlış sonuç -1 puandır.")
print(
    "-------------------------------------------------------------------------------------------------------------------------------------")

score = 0

answer = "e"
while answer == "e":
    if score >= 0 and score <= 20:
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        operate_number = random.randint(1, 4)

        if operate_number == 1:
            result = number_1 + number_2
            question = int(input("{} + {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 2
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))
        elif operate_number == 2:
            result = number_1 - number_2
            question = int(input("{} - {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 2
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))
        elif operate_number == 3:
            result = number_1 * number_2
            question = int(input("{} * {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 2
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))
        elif operate_number == 4:
            result = number_1 // number_2
            question = int(input("{} / {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 2
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))

        print("Dört İşlem Sorularına Devam Etmek İster Misin {}?".format(name))
        answer = input("Cevabınız Evet ise [e], Hayır ise herhangi bir tuşa basınız. (Lütfen Küçük Harf Kullanınız.): ")

        if score > 20 and score < 40:
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------")
            print(
                "Tebrikler 2. Seviyeye Geçtiniz. Bu seviyede 1 ila 100 arasındaki sayılarla dört işlem yapacaksınız. Kolay Gelsin.")
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------")
        elif score >= 0 and score <= 20:
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------")


    elif score >= 21 and score <= 40:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        operate_number = random.randint(1, 4)

        if operate_number == 1:
            result = number_1 + number_2
            question = int(input("{} + {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 2
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))
        elif operate_number == 2:
            result = number_1 - number_2
            question = int(input("{} - {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 2
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))
        elif operate_number == 3:
            result = number_1 * number_2
            question = int(input("{} * {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 2
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))
        elif operate_number == 4:
            result = number_1 // number_2
            question = int(input("{} / {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 2
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))

        print("Dört İşlem Sorularına Devam Etmek İster Misin {}?".format(name))
        answer = input("Cevabınız Evet ise [e], Hayır ise herhangi bir tuşa basınız. (Lütfen Küçük Harf Kullanınız.):")

        if score > 40 and score < 1000000000:
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------")
            print(
                "Tebrikler 3. Seviyeye Geçtiniz. Bu seviyede 1 ila 1000 arasındaki sayılarla dört işlem yapacaksınız. Gerçekten zorlanabilirsiniz. Kolay Gelsin.")
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------")
        elif score >= 0 and score <= 20:
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------")

    elif score >= 41 and score <= 100000000:
        number_1 = random.randint(1, 1000)
        number_2 = random.randint(1, 1000)
        operate_number = random.randint(1, 4)

        if operate_number == 1:
            result = number_1 + number_2
            question = int(input("{} + {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 5
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))
        elif operate_number == 2:
            result = number_1 - number_2
            question = int(input("{} - {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 5
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))
        elif operate_number == 3:
            result = number_1 * number_2
            question = int(input("{} * {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 5
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))
        elif operate_number == 4:
            result = number_1 // number_2
            question = int(input("{} / {} = ? işleminin sonucu kaçtır?".format(number_1, number_2)))
            if result == question:
                score = score + 5
                print("Tebrikler Doğru Bildiniz. Şuanki Puanınız: {}".format(score))
            else:
                score = score - 1
                print("Yanlış Bildiniz. Şuanki Puanınız: {}".format(score))

        print("Dört İşlem Sorularına Devam Etmek İster Misin {}?".format(name))
        answer = input("Cevabınız Evet ise [e], Hayır ise herhangi bir tuşa basınız. (Lütfen Küçük Harf Kullanınız.):")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------")









