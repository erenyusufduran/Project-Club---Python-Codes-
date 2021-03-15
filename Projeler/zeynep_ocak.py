print("-------------------------------------------")
print("             İŞLEM OYUNU                   ")
print("-------------------------------------------")

kullaniciadi=input("Kullanıcı adınızı giriniz: ")
print("Zorluk seviyeleri")
print("1.seviye")
print("2.seviye")
print("3.seviye")
zorluk=input("Zorluk seviyesini seçiniz: ")
puan=0
sonuc=""
for i in range(1,11):
    if zorluk=="1":
        import random
        sayi1=random.randint(1,10)
        sayi2=random.randint(1,10)
        islemler=["+","-"]
        isaret=random.choice(islemler)
               
    elif zorluk=="2":
        import random
        sayi1=random.randint(10,50)
        sayi2=random.randint(10,50)
        islemler=["+","-","*"]
        isaret=random.choice(islemler)
    else:
        import random
        sayi1=random.randint(50,100)
        sayi2=random.randint(50,100)
        islemler=["+","-","*","/"]
        isaret=random.choice(islemler)
            
    if isaret=="+":
        sonuc=sayi1+sayi2
    elif isaret=="-":
        sonuc=sayi1-sayi2
    elif isaret=="*":
        sonuc=sayi1*sayi2
    else:
        sonuc==sayi1//sayi2
            
    cevap=int(input("{}{}{}= ? işleminin sonucu kaçtır?".format(sayi1,isaret,sayi2)))
  
    if cevap==sonuc:
        print("Bildin")
        puan += 10
    else:
        print("Bilemedin")
        puan -= 10
    
print("--------------------------------------------")
print("Tebrikler {} .Oyun Sonu Toplam Puanın: {} ".format(kullaniciadi,puan))


    
    

    
    
    
   