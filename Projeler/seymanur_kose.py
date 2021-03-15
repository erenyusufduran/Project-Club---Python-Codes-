import random
isim=input("Merhaba oyuna geçmeden önce adýný öðrenebilir miyim:")
print("\nMatematik Oyununa Hoþ Geldin {}!!!\nDoðru cevaplarýn için 1.seviyede 5 puan,2.seviyede 10 puan,3.seviyede 15 puan; yanlýþ cevaplarýn için ise 1.seviyede 0 puan, 2.seviyede -5 puan, 3.seviyede -10 puan alacaksýn.".format(isim))
mesaj=input("[1].Seviye(Kolay)\n[2].Seviye(Orta)\n[3].Seviye(Zor)\nHangi seviyede oynamak istersin?:")
puan=0
oyun=0
while True:
    oyun+=1
    if mesaj=="1":
        tamSayi1=random.randint(1,10)
        tamSayi2=random.randint(1,10)
        islem=[tamSayi1+tamSayi2,tamSayi1-tamSayi2]
        sonuc=random.choice(islem)
        if sonuc==tamSayi1+tamSayi2:
            cevap=int(input("{}+{}= \n iþleminin sonucu nedir?:\n".format(tamSayi1,tamSayi2)))
            if cevap==sonuc:
                print("Doðru bildin!!!")
                puan+=5
            else:
                print("Bilemedin")
        else:
            cevap=int(input("{}-{}= \n iþleminin sonucu nedir?:\n".format(tamSayi1,tamSayi2)))
            if cevap==sonuc:
                print("Doðru bildin!!!")
                puan+=5
            else:
                print("Bilemedin")
    elif mesaj=="2":
        tamSayi1=random.randint(1,50)
        tamSayi2=random.randint(1,50)
        islem=[tamSayi1+tamSayi2,tamSayi1-tamSayi2,tamSayi1*tamSayi2]
        sonuc=random.choice(islem)
        if sonuc==tamSayi1+tamSayi2:
            cevap=int(input("{}+{}= \n iþleminin sonucu nedir?:\n".format(tamSayi1,tamSayi2)))
            if cevap==sonuc:
                print("Doðru bildin!!!")
                puan+=10
            else:
                print("Bilemedin")
                puan-=5
        elif sonuc==tamSayi1*tamSayi2:
            cevap=int(input("{}*{}= \n iþleminin sonucu nedir?:\n".format(tamSayi1,tamSayi2)))
            if cevap==sonuc:
                print("Doðru bildin!!!")
                puan+=10
            else:
                print("Bilemedin")
                puan-=5
        else:
            cevap=int(input("{}-{}= \n iþleminin sonucu nedir?:\n".format(tamSayi1,tamSayi2)))
            if cevap==sonuc:
                print("Doðru bildin!!!")
                puan+=10
            else:
                print("Bilemedin")
                puan-=5
    else:
        tamSayi1=random.randint(1,100)
        tamSayi2=random.randint(1,100)
        islem=[tamSayi1+tamSayi2,tamSayi1-tamSayi2,tamSayi1*tamSayi2,tamSayi1//tamSayi2]
        sonuc=random.choice(islem)
        if sonuc==tamSayi1+tamSayi2:
            cevap=int(input("{}+{}= \n iþleminin sonucu nedir?:\n".format(tamSayi1,tamSayi2)))
            if cevap==sonuc:
                print("Doðru bildin!!!")
                puan+=15
            else:
                print("Bilemedin")
                puan-=10
        elif sonuc==tamSayi1*tamSayi2:
            cevap=int(input("{}*{}= \n iþleminin sonucu nedir?:\n".format(tamSayi1,tamSayi2)))
            if cevap==sonuc:
                print("Doðru bildin!!!")
                puan+=15
            else:
                print("Bilemedin")
                puan-=10
        elif sonuc==tamSayi1//tamSayi2:
            cevap=int(input("{}//{}= \n iþleminin sonucu nedir?:\n".format(tamSayi1,tamSayi2)))
            if cevap==sonuc:
                print("Doðru bildin!!!")
                puan+=15
            else:
                print("Bilemedin")
                puan-=10
        else:
            cevap=int(input("{}-{}= \n iþleminin sonucu nedir?:\n".format(tamSayi1,tamSayi2)))
            if cevap==sonuc:
                print("Doðru bildin!!!")
                puan+=15
            else:
                print("Bilemedin")
                puan-=10
    mesaj2=input("Devam etmek istiyor musun? [e]vet/[h]ayýr:")
    if mesaj2=="h":
        if puan>0:
            print("Tebrikler {}!!{} oyunda {} puan kazandýn.".format(isim,oyun,puan))
        else:
            print("Maalesef {}!!Daha çok çalýþmalýsýn. {} oyunda {} puan kazandýn.".format(isim,oyun,puan))
        break
    else:
        mesaj=input("[1].Seviye(Kolay)\n[2].Seviye(Orta)\n[3].Seviye(Zor)\nHangi seviyede oynamak istersin?:")
