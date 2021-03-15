from random import randint, choice
print ("Matematik oyununa hoşgeldiniz")
print ("dört işlem: 1=kolay,2=orta,3=zor")
print ("üs soruları: 4=kolay,5=zor")
zorluk=int(input("zorluk seviyesi seçin:"))
liste1 = ["toplama","çıkarma"]
liste2 = ["toplama","çıkarma","çarpma","bölme"]
dogru_cevap_sayısı=0

if zorluk== 1 :
    soru_sayısı = int(input("kaç soru çözmek istersiniz:"))
    soru_numarası=0
    while (soru_numarası< soru_sayısı):
        soru_numarası = soru_numarası+1
        sayı1 = randint(0, 10)
        sayı2 = randint(0, 10)
        soru = (choice(liste1))
        if soru == "toplama":
            soru1 = "{} + {}".format(sayı1, sayı2)
            print(soru1)
            dogru_cevap = sayı1 + sayı2
            kullanıcı_cevabı = int(input("cevap nedir?"))
            if dogru_cevap == kullanıcı_cevabı:
                dogru_cevap_sayısı = dogru_cevap_sayısı +1
                print("doğru cevabı buldunuz tebrikler!")
            elif dogru_cevap != kullanıcı_cevabı:
                yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
                print(yanlış_cevaba_cevap)
        if soru == "çıkarma":
            soru = "{} - {}".format(sayı1, sayı2)
            print(soru)
            dogru_cevap = sayı1 - sayı2
            kullanıcı_cevabı = int(input("cevap nedir?"))
            if dogru_cevap == kullanıcı_cevabı:
                dogru_cevap_sayısı= dogru_cevap_sayısı+1
                print("doğru cevabı buldunuz tebrikler!")
            elif dogru_cevap != kullanıcı_cevabı:
                yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
                print(yanlış_cevaba_cevap)
    print("sonucunuz kontrol ediliyor...")
    print("hesaplandı!")
    kullanıcı_puanı = "puanınız:{}/{}" .format(dogru_cevap_sayısı,soru_sayısı)
    print (kullanıcı_puanı)
    soru_sayısı_bölü_2 = soru_sayısı / 2
    if dogru_cevap_sayısı >= soru_sayısı_bölü_2 and dogru_cevap_sayısı != soru_sayısı:
        print("BAŞARILI SONUÇ")
        print("iyi bir sonuç çıkardınız")
    if soru_sayısı == dogru_cevap_sayısı:
        print ("BAŞARILI SONUÇ")
        print("***çok iyi bir sonuç çıkardınız***")
    if dogru_cevap_sayısı < soru_sayısı_bölü_2:
        print("BAŞARISIZ SONUÇ")
        print("kötü bir sonuç çıkardınız,daha çok çalışmanızı öneririz")

if zorluk== 2 :
    soru_sayısı = int(input("kaç soru çözmek istersiniz:"))
    soru_numarası = 0
    while (soru_numarası < soru_sayısı):
        soru_numarası = soru_numarası + 1
        sayı1 = randint(10, 50)
        sayı2 = randint(0, 50)
        soru = (choice(liste2))
        if soru == "toplama":
            soru1 = "{} + {}".format(sayı1, sayı2)
            print(soru1)
            dogru_cevap = sayı1 + sayı2
            kullanıcı_cevabı = int(input("cevap nedir?"))
            if dogru_cevap == kullanıcı_cevabı:
                dogru_cevap_sayısı = dogru_cevap_sayısı + 1
                print("doğru cevabı buldunuz tebrikler!")
            elif dogru_cevap != kullanıcı_cevabı:
                yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
                print(yanlış_cevaba_cevap)
        if soru == "çıkarma":
            soru = "{} - {}".format(sayı1, sayı2)
            print(soru)
            dogru_cevap = sayı1 - sayı2
            kullanıcı_cevabı = int(input("cevap nedir?"))
            if dogru_cevap == kullanıcı_cevabı:
                dogru_cevap_sayısı = dogru_cevap_sayısı + 1
                print("doğru cevabı buldunuz tebrikler!")
            elif dogru_cevap != kullanıcı_cevabı:
                yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
                print(yanlış_cevaba_cevap)
        if soru == "çarpma":
            soru = "{} * {}".format(sayı1, sayı2)
            print(soru)
            dogru_cevap = sayı1 * sayı2
            kullanıcı_cevabı = int(input("cevap nedir?"))
            if dogru_cevap == kullanıcı_cevabı:
                dogru_cevap_sayısı = dogru_cevap_sayısı + 1
                print("doğru cevabı buldunuz tebrikler!")
            elif dogru_cevap != kullanıcı_cevabı:
                yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
                print(yanlış_cevaba_cevap)
        if soru == "bölme":
            print("ÖNEMLİ! bu soruda sadece bölünenin içinde kaç tane bölen olduğunu yazmanız yeterlidir")
            soru = "{} / {}".format(sayı1, sayı2)
            print(soru)
            dogru_cevap = sayı1 // sayı2
            kullanıcı_cevabı = int(input("cevap nedir?"))
            if dogru_cevap == kullanıcı_cevabı:
                dogru_cevap_sayısı = dogru_cevap_sayısı + 1
                print("doğru cevabı buldunuz tebrikler!")
            elif dogru_cevap != kullanıcı_cevabı:
                yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
                print(yanlış_cevaba_cevap)
    print("sonucunuz kontrol ediliyor...")
    print("hesaplandı!")
    kullanıcı_puanı = "puanınız:{}/{}".format(dogru_cevap_sayısı, soru_sayısı)
    print(kullanıcı_puanı)
    soru_sayısı_bölü_2 = soru_sayısı / 2
    if dogru_cevap_sayısı >= soru_sayısı_bölü_2 and dogru_cevap_sayısı != soru_sayısı:
        print("BAŞARILI SONUÇ")
        print("iyi bir sonuç çıkardınız")
    if soru_sayısı == dogru_cevap_sayısı:
        print ("BAŞARILI SONUÇ")
        print("***çok iyi bir sonuç çıkardınız***")
    if dogru_cevap_sayısı < soru_sayısı_bölü_2:
        print("BAŞARISIZ SONUÇ")
        print("kötü bir sonuç çıkardınız,daha çok çalışmalısınız")
if zorluk== 3 :
    soru_sayısı = int(input("kaç soru çözmek istersiniz:"))
    soru_numarası = 0
    while (soru_numarası < soru_sayısı):
        soru_numarası = soru_numarası + 1
        sayı1 = randint(40, 100)
        sayı2 = randint(0, 75)
        soru = (choice(liste2))
        if soru == "toplama":
            soru1 = "{} + {}".format(sayı1, sayı2)
            print(soru1)
            dogru_cevap = sayı1 + sayı2
            kullanıcı_cevabı = int(input("cevap nedir?"))
            if dogru_cevap == kullanıcı_cevabı:
                dogru_cevap_sayısı = dogru_cevap_sayısı + 1
                print("doğru cevabı buldunuz tebrikler!")
            elif dogru_cevap != kullanıcı_cevabı:
                yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
                print(yanlış_cevaba_cevap)
        if soru == "çıkarma":
            soru = "{} - {}".format(sayı1, sayı2)
            print(soru)
            dogru_cevap = sayı1 - sayı2
            kullanıcı_cevabı = int(input("cevap nedir?"))
            if dogru_cevap == kullanıcı_cevabı:
                dogru_cevap_sayısı = dogru_cevap_sayısı + 1
                print("doğru cevabı buldunuz tebrikler!")
            elif dogru_cevap != kullanıcı_cevabı:
                yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
                print(yanlış_cevaba_cevap)
        if soru == "çarpma":
            soru = "{} * {}".format(sayı1, sayı2)
            print(soru)
            dogru_cevap = sayı1 * sayı2
            kullanıcı_cevabı = int(input("cevap nedir?"))
            if dogru_cevap == kullanıcı_cevabı:
                dogru_cevap_sayısı = dogru_cevap_sayısı + 1
                print("doğru cevabı buldunuz tebrikler!")
            elif dogru_cevap != kullanıcı_cevabı:
                yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
                print(yanlış_cevaba_cevap)
        if soru == "bölme":
            print("ÖNEMLİ!  bu soruda sadece bölünenin içinde kaç tane bölen olduğunu yazmanız yeterlidir")
            soru = "{} / {}".format(sayı1, sayı2)
            print(soru)
            dogru_cevap = sayı1 // sayı2
            kullanıcı_cevabı = int(input("cevap nedir?"))
            if dogru_cevap == kullanıcı_cevabı:
                dogru_cevap_sayısı = dogru_cevap_sayısı + 1
                print("doğru cevabı buldunuz tebrikler!")
            elif dogru_cevap != kullanıcı_cevabı:
                yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
                print(yanlış_cevaba_cevap)
    print("sonucunuz kontrol ediliyor...")
    print("hesaplandı!")
    kullanıcı_puanı = "puanınız:{}/{}".format(dogru_cevap_sayısı, soru_sayısı)
    print(kullanıcı_puanı)
    soru_sayısı_bölü_2 = soru_sayısı / 2
    if dogru_cevap_sayısı >= soru_sayısı_bölü_2 and dogru_cevap_sayısı != soru_sayısı:
        print("BAŞARILI SONUÇ")
        print("iyi bir sonuç çıkardınız")
    if soru_sayısı == dogru_cevap_sayısı:
        print ("BAŞARILI SONUÇ")
        print("***çok iyi bir sonuç çıkardınız***")
    if dogru_cevap_sayısı < soru_sayısı_bölü_2:
        print("BAŞARISIZ SONUÇ")
        print("kötü bir sonuç çıkardınız,daha çok çalışmalısınız")
if zorluk== 4 :
    soru_sayısı = int(input("kaç soru çözmek istersiniz:"))
    soru_numarası=0
    while (soru_numarası< soru_sayısı):
        soru_numarası = soru_numarası+1
        sayı1 = randint(0, 10)
        sayı2 = randint(0, 6)
        soru1 = "{} üssü {}".format(sayı1, sayı2)
        print(soru1)
        dogru_cevap = sayı1 ** sayı2
        kullanıcı_cevabı = int(input("cevap nedir?"))
        if dogru_cevap == kullanıcı_cevabı:
            dogru_cevap_sayısı = dogru_cevap_sayısı +1
            print("doğru cevabı buldunuz tebrikler!")
        elif dogru_cevap != kullanıcı_cevabı:
            yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
            print(yanlış_cevaba_cevap)
    print("sonucunuz kontrol ediliyor...")
    print("hesaplandı!")
    kullanıcı_puanı = "puanınız:{}/{}" .format(dogru_cevap_sayısı,soru_sayısı)
    print (kullanıcı_puanı)
    soru_sayısı_bölü_2 = soru_sayısı / 2

    if dogru_cevap_sayısı >= soru_sayısı_bölü_2 and dogru_cevap_sayısı != soru_sayısı:
        print("BAŞARILI SONUÇ")
        print("iyi bir sonuç çıkardınız")
    if soru_sayısı == dogru_cevap_sayısı:
        print ("BAŞARILI SONUÇ")
        print("***çok iyi bir sonuç çıkardınız***")
    if dogru_cevap_sayısı < soru_sayısı_bölü_2:
        print("BAŞARISIZ SONUÇ")
        print("kötü bir sonuç çıkardınız,daha çok çalışmalısınız")
if zorluk== 5 :
    soru_sayısı = int(input("kaç soru çözmek istersiniz:"))
    soru_numarası=0
    while (soru_numarası< soru_sayısı):
        soru_numarası = soru_numarası+1
        sayı1 = randint(10, 30)
        sayı2 = randint(2, 6)
        soru1 = "{} üssü {}".format(sayı1, sayı2)
        print(soru1)
        dogru_cevap = sayı1 ** sayı2
        kullanıcı_cevabı = int(input("cevap nedir?"))
        if dogru_cevap == kullanıcı_cevabı:
            dogru_cevap_sayısı = dogru_cevap_sayısı +1
            print("doğru cevabı buldunuz tebrikler!")
        elif dogru_cevap != kullanıcı_cevabı:
            yanlış_cevaba_cevap = "mallesef yanlış cevap. doğru cevap:{}".format(dogru_cevap)
            print(yanlış_cevaba_cevap)
    print("sonucunuz kontrol ediliyor...")
    print("hesaplandı!")
    kullanıcı_puanı = "puanınız:{}/{}" .format(dogru_cevap_sayısı,soru_sayısı)
    print (kullanıcı_puanı)
    soru_sayısı_bölü_2 = soru_sayısı / 2

    if dogru_cevap_sayısı >= soru_sayısı_bölü_2 and dogru_cevap_sayısı != soru_sayısı:
        print("BAŞARILI SONUÇ")
        print("iyi bir sonuç çıkardınız")
    if soru_sayısı == dogru_cevap_sayısı:
        print ("BAŞARILI SONUÇ")
        print("***çok iyi bir sonuç çıkardınız***")
    if dogru_cevap_sayısı < soru_sayısı_bölü_2:
        print("BAŞARISIZ SONUÇ")
        print("kötü bir sonuç çıkardınız,daha çok çalışmalısınız")

