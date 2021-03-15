import random
print("---------MATEMATİK OYUNUNA HOŞGELDİNİZ---------")
oyuncuListesi = []
oyuncuSayisi = input("Oyuncu sayısı giriniz:")
print("Oyuncu adlarını giriniz:")
i =0
while i<int(oyuncuSayisi):
    isim = input()
    oyuncuListesi.append(isim)
    i+=1
zorluk = input("Zorluk seçiniz(Kolay:1\tOrta:2\tZor:3):")
print("Oyun başlıyor...")
a=0
islemlerKolay = ['+','-']
islemler = ['+','-','*','/']
txt = "{} {} {} = "
txt0 = "{} isimli oyuncunun sırası"
while a<3:
    b=0
    while b<len(oyuncuListesi):
        print(txt0.format(oyuncuListesi[b]))
        if int(zorluk) == 1:
            sayi1 = (random.randint(1,50))
            sayi2 = (random.randint(1,50))
            islem = random.choice(islemlerKolay)
        elif int(zorluk) == 2:
            sayi1 = (random.randint(1,50))
            sayi2 = (random.randint(1,50))
            islem = random.choice(islemler)
        elif int(zorluk) == 3:
            sayi1 = (random.randint(50,100))
            sayi2 = (random.randint(50,100))
            islem = random.choice(islemler)
        if islem == '+':
            sonuc = sayi1 + sayi2
        elif islem == '-':
            sonuc = sayi1 - sayi2
        elif islem == '*':
            sonuc = sayi1*sayi2
        elif islem == '/':
            sonuc = sayi1 / sayi2
        print(txt.format(sayi1,islem,sayi2))
        cevap = input()
        if int(cevap) == int(sonuc):
            if a!=2:
                print("Sonraki soruya geçemeye hak kazandınız!")
        else:
            print("Elendiniz!")
            oyuncuListesi.pop(b)
            b-=1
        b+=1
    a+=1
txt1= "Oyun bitti...\nKazananlar:\n{}\nTebrikler..."
txt2="Oyun bitti...\nKazanan:\n{}\nTebrikler..."
if len(oyuncuListesi) == 0:
    print("Kimse kazanamadı. Tekrar deneyin.")
elif len(oyuncuListesi) == 1:
    print(txt2.format(oyuncuListesi))
else:
    print(txt1.format(oyuncuListesi))