import random

print("Bölme işlemlerinde küsürat için . ve .'dan sonra bir sayı kullanınız")
def islemler(sayi1,sayi2,islem):
    if islem == "/":
        cevap = round(eval((str(sayi1) + islem + str(sayi2))),1)
        if (sayi1%sayi2==0):
            cevap=int(cevap)
    else:
        cevap = eval((str(sayi1) + islem + str(sayi2)))
    return cevap

while True:
    print('Çıkmak için (ctrl + c) yapınız\n')
    zorluk = int(input("Zorluk seviyesi seçiniz\n1)Kolay\n2)Orta\n3)Zor\n"))

    
    for i in range(0,5):
        if zorluk == 1:
            islemler1 = ['+', '-', '*', '/']
            islem = random.choice(islemler1)
            sayi1 = random.randint(0,30)
            sayi2 = random.randint(0,30)
            cevap=islemler(sayi1,sayi2,islem)
            sonuc = input("{} {} {} işleminin sonucu nedir?".format(sayi1,islem,sayi2))
            if sonuc == str(cevap):
                print('Tebrikler bildiniz.')
            else:
                print('Bilemediniz :(')
        elif zorluk == 2:
            islemler1 = ['+', '-', '*', '/']
            islem = random.choice(islemler1)
            sayi1 = random.randint(30,60)
            sayi2 = random.randint(30,60)
            cevap=islemler(sayi1,sayi2,islem)
            sonuc = input("{} {} {} işleminin sonucu nedir?".format(sayi1,islem,sayi2))
            if sonuc == str(cevap):
                print('Tebrikler bildiniz.')
            else:
                print('Bilemediniz :(')
        elif zorluk == 3:
            islemler1 = ['+', '-', '*', '/']
            islem = random.choice(islemler1)
            sayi1 = random.randint(60,100)
            sayi2 = random.randint(60,100)
            cevap=islemler(sayi1,sayi2,islem)
            sonuc = input("{} {} {} işleminin sonucu nedir?".format(sayi1,islem,sayi2))
            if sonuc == str(cevap):
                print('Tebrikler bildiniz.')
            else:
                print('Bilemediniz :(')
        else:
            print("Geçersiz sayı girdiniz.")
            break
        
    
   