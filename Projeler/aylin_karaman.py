import random

seviyeler = """
(1) kolay
(2) orta
(3) zor
"""
print(seviyeler)

anahtar = 1

while anahtar == 1:
    x = input("Oynamak istediğiniz zorluk seviyesini girin (Çıkmak için 0): ")
    if x == "0":
        print("Çıkılıyor...")
        anahtar = 0
    elif x=="1": #seviye1
        sayi1=random.randint(1,10)
        sayi2=random.randint(1,10)
        islem1=["+","-"]
        a=random.choice(islem1)
        if a==islem1[0]:
            sonuc1=sayi1+sayi2
        else:
            sonuc1=sayi1-sayi2
        while x=="1":
            cevap1=int(input("{}{}{}=? işleminin sonucu kaçtır? ".format(sayi1,a,sayi2)))
            if cevap1==sonuc1:
                print("Tebrikler, bildin!")
                y=input("Tekrar oynamak ister misin? Cevabın evet ise 1 yaz: ")
                if y == "1":
                    x = 1
                else:
                    print("Çıkılıyor...")
                    x = 0
                    anahtar = 0
            else:
                print("Bilemedin. Tekrar dene!")
    elif x=="2": #seviye2
        sayi3=random.randint(10,50)
        sayi4=random.randint(10,50)
        islem2=["+","-","*"]
        b=random.choice(islem2)
        if b==islem2[0]:
            sonuc2=sayi3+sayi4
        elif b==islem2[1]:
            sonuc2=sayi3-sayi4
        else:
            sonuc2=sayi3*sayi4
        while x=="2":
            cevap2=int(input("{}{}{}=? işleminin sonucu kaçtır? ".format(sayi3,b,sayi4)))
            if cevap2==sonuc2:
                print("Tebrikler, bildin!")
                y=input("Tekrar oynamak ister misin? Cevabın evet ise 1 yaz: ")
                if y == "1":
                    x = 2
                else:
                    print("Çıkılıyor...")
                    x = 0
                    anahtar = 0
            else:
                print("Bilemedin. Tekrar dene!")
    elif x=="3": #seviye3
        sayi5=random.randint(50,100)
        sayi6=random.randint(50,100)
        islem3=["+","-","*","//"]
        c=random.choice(islem3)
        if c==islem3[0]:
            sonuc3=sayi5+sayi6
        elif c==islem3[1]:
            sonuc3=sayi5-sayi6
        elif c==islem3[2]:
            sonuc3=sayi5*sayi6
        else:
            sonuc3=sayi5//sayi6
        while x=="3":
            cevap3=int(input("{}{}{}=? işleminin sonucu kaçtır? ".format(sayi5,c,sayi6)))
            if cevap3==sonuc3:
                print("Tebrikler, bildin!")
                y=input("Tekrar oynamak ister misin? Cevabın evet ise 1 yaz: ")
                if y == "1":
                    x = 3
                else:
                    print("Çıkılıyor...")
                    x = 0
                    anahtar = 0
            else:
                print("Bilemedin. Tekrar dene!")
    else:
        print("Yanlış seviye girdiniz. Tekrar deneyin! ")