import random
islemler=["+","-","/","x"]
print("Zorluk seviyesini seçiniz:\n1-Kolay\n2-Orta\n3-Zor\n")
zorluk=input()
print("Soru sayısını yazınız")
soru=int(input())
dogrusayisi=0
i=0
for i in range(soru):
    islem=random.choice(islemler)
    if islem=="x":
        if zorluk=="1":
            sayi1=random.randint(1,10)
            sayi2=random.randint(1,10)
        elif zorluk=="2":
            sayi1=random.randint(5,20)
            sayi2=random.randint(5,20)
        elif zorluk=="3":
            sayi1=random.randint(10,30)
            sayi2=random.randint(10,30)
    elif islem=="+" or islem=="-":
        if zorluk=="1":
            sayi1=random.randint(5,30)
            sayi2=random.randint(5,30)
        elif zorluk=="2":
            sayi1=random.randint(25,100)
            sayi2=random.randint(25,100)
        elif zorluk=="3":
            sayi1=random.randint(50,250)
            sayi2=random.randint(50,250)
    elif islem=="/":
        if zorluk=="1":
            sayi1=random.randint(1,5)
            sayi2=random.randint(1,5)
        elif zorluk=="2":
            sayi1=random.randint(1,10)
            sayi2=random.randint(1,10)
        elif zorluk=="3":
            sayi1=random.randint(1,20)
            sayi2=random.randint(1,20)
    if islem=="+":
        sonuc=sayi1+sayi2
    elif islem=="-":
        if sayi2>sayi1:
            a= sayi1
            sayi1= sayi2
            sayi2=a
        sonuc=sayi1-sayi2
    elif islem=="x":
        sonuc=sayi1*sayi2
    elif islem=="/":
        sonuc=sayi1
        sayi1= sayi1*sayi2
    print(sayi1,islem,sayi2,"= ?\n")
    cevap=int(input())
    if cevap==sonuc:
        print("DOĞRU")
        dogrusayisi= dogrusayisi+1
    else:
        print("YANLIS")

print("Tebrikler tüm soruları yanıtladınız.\nSoru Sayısı:\t",soru,"\nDoğru Sayısı:\t",dogrusayisi)
input("Çıkış yapmak için enter'a basınız")