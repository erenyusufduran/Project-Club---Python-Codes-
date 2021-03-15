#Level 1: Pozitif sayılar için 4 işlem; 55 puan ve üzerinde negatif sayılar ile 4 işlem
#Level 2: Kare alma, Mod alma, Tam Bölünen bulma

level=input("Kaçıncı level?\nLevel 1 için:L1\nLevel 2 için:L2\ngiriniz:")
puan=0
while True:
    if level=="L1":
        import random
        birinci_sayi= random.randint(0,10)
        ikinci_sayi = random.randint(0,10)
        islem=["+","-","*","/"]
        pc_sectigi_islem= random.choice(islem)
        print("{}{}{}=?".format(birinci_sayi,pc_sectigi_islem,ikinci_sayi))
        kullanici_sonuc=int(input("Yukarıdaki işlemin sonucu kaçtır?:" ))
        if pc_sectigi_islem==islem[0]:
            sonuc=birinci_sayi+ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan+=5
                print("Toplam Puan:",puan)
            else:
                print("YANLIŞ CEVAP, OYUN SONA ERDİ!")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:",puan)
                break
        elif pc_sectigi_islem==islem[1]:
            sonuc=birinci_sayi-ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan+=5
                print("Toplam Puan:",puan)
            else:
                print("YANLIŞ CEVAP")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:", puan)
                break
        elif pc_sectigi_islem==islem[2]:
            sonuc=birinci_sayi*ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan+=5
                print("Toplam Puan:", puan)
            else:
                print("YANLIŞ CEVAP")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:", puan)
                break
        elif pc_sectigi_islem==islem[3]:
            sonuc=birinci_sayi/ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan += 5
                print("Toplam Puan:", puan)
            else:
                print("YANLIŞ CEVAP")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:", puan)
                break

    if puan>=55:
        import random
        birinci_sayi= random.randint(-10,0)
        ikinci_sayi = random.randint(-10,0)
        islem=["+","-","*","/"]
        pc_sectigi_islem= random.choice(islem)
        print("-----NEGATİF SAYILAR-----")
        print("({}){}({})=?".format(birinci_sayi,pc_sectigi_islem,ikinci_sayi))
        kullanici_sonuc=int(input("Yukarıdaki işlemin sonucu kaçtır?:" ))

        if pc_sectigi_islem==islem[0]:
            sonuc=birinci_sayi+ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan+=5
                print("Toplam Puan:",puan)
            else:
                print("YANLIŞ CEVAP, OYUN SONA ERDİ!")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:",puan)
                break
        elif pc_sectigi_islem==islem[1]:
            sonuc=birinci_sayi-ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan+=5
                print("Toplam Puan:",puan)
            else:
                print("YANLIŞ CEVAP")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:", puan)
                break
        elif pc_sectigi_islem==islem[2]:
            sonuc=birinci_sayi*ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan+=5
                print("Toplam Puan:", puan)
            else:
                print("YANLIŞ CEVAP")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:", puan)
                break
        elif pc_sectigi_islem==islem[3]:
            sonuc=birinci_sayi/ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan += 5
                print("Toplam Puan:", puan)
            else:
                print("YANLIŞ CEVAP")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:", puan)
                break
    if level=="L2":
        import random
        birinci_sayi= random.randint(0,5)
        ikinci_sayi = random.randint(0,5)
        islem=["**","%","//"]
        pc_sectigi_islem= random.choice(islem)
        print("({}){}({})=?".format(birinci_sayi,pc_sectigi_islem,ikinci_sayi))
        kullanici_sonuc=int(input("Yukarıdaki işlemin sonucu kaçtır?:" ))
        if pc_sectigi_islem==islem[0]:
            sonuc=birinci_sayi**ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan+=5
                print("Toplam Puan:",puan)
            else:
                print("YANLIŞ CEVAP, OYUN SONA ERDİ!")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:",puan)
                break
        elif pc_sectigi_islem==islem[1]:
            sonuc=birinci_sayi%ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan+=5
                print("Toplam Puan:",puan)
            else:
                print("YANLIŞ CEVAP")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:", puan)
                break
        elif pc_sectigi_islem==islem[2]:
            sonuc=birinci_sayi//ikinci_sayi
            if sonuc==kullanici_sonuc:
                print("TEBRİKLER, DOĞRU CEVAP")
                puan+=5
                print("Toplam Puan:", puan)
            else:
                print("YANLIŞ CEVAP")
                print("İşlemin Sonucu:", sonuc)
                print("Kazandığınız Puan Toplamı:", puan)
                break
        if puan<50:
            print("Tekrar deneyiniz")
        else:
            print("BAŞARILI!")