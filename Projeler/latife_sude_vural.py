# Beykent Üniversitesi - Python Projesi /Latife Sude Vural

print('''-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Rastgele sayılarla dört işlem oyununa hoşgeldiniz!
______________________________________________________
Lütfen istediğiniz zorluk seviyesini yazın:           |
Basit                                                 |
Orta                                                  |
Zor                                                   |
Lütfen seçmek istediğiniz işlemin numarasını girin:   |
1- Toplama                                            |
2- Çıkarma                                            |
3- Çarpma                                             |
4- Bölme                                              |
(Oyundan çıkış yapmak için lütfen                     |
zorluk seviyesine ve işlem numarasına 0 girin)        |
______________________________________________________|

-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*''')
import random
while True:
    islem_seviye = input("Lütfen istediğiniz zorluk seviyesini yazın:")
    islem_no = int(input("Lütfen seçmek istediğiniz işlemin numarasını girin:"))
    if(islem_seviye == "Basit" and islem_no == 1):
        sayı1 = random.randint(1,11)
        sayı2 = random.randint(1,11)
        cevap = sayı1+sayı2
        islem = "+"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")    
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue
        
    elif(islem_seviye =="Basit" and islem_no == 2):
        sayı1 = random.randint(1,11)
        sayı2 = random.randint(1,11)
        cevap = sayı1-sayı2
        islem = "-"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue
        
    elif(islem_seviye =="Basit" and islem_no == 3):
        sayı1 = random.randint(1,11)
        sayı2 = random.randint(1,11)
        cevap = sayı1*sayı2
        islem = "*"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue

    elif(islem_seviye =="Basit" and islem_no == 4):
        sayı1 = random.randint(1,11)
        sayı2 = random.randint(1,11)
        cevap = sayı1/sayı2
        islem = "/"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue

    
    elif(islem_seviye == "Orta" and islem_no == 1):
        sayı1 = random.randint(10,101)
        sayı2 = random.randint(10,101)
        cevap = sayı1+sayı2
        islem = "+"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue
        
    elif(islem_seviye =="Orta" and islem_no == 2):
        sayı1 = random.randint(10,101)
        sayı2 = random.randint(10,101)
        cevap = sayı1-sayı2
        islem = "-"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue
        
    elif(islem_seviye =="Orta" and islem_no == 3):
        sayı1 = random.randint(10,101)
        sayı2 = random.randint(10,101)
        cevap = sayı1*sayı2
        islem = "*"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue 

    elif(islem_seviye =="Orta" and islem_no == 4):
        sayı1 = random.randint(10,101)
        sayı2 = random.randint(10,101)
        cevap = sayı1/sayı2
        islem = "/"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue
    
    elif(islem_seviye == "Zor" and islem_no == 1):
        sayı1 = random.randint(100,1001)
        sayı2 = random.randint(100,1001)
        cevap = sayı1+sayı2
        islem = "+"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue
        
    elif(islem_seviye =="Zor" and islem_no == 2):
        sayı1 = random.randint(100,1001)
        sayı2 = random.randint(100,1001)
        cevap = sayı1-sayı2
        islem = "-"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue
        
    elif(islem_seviye =="Zor" and islem_no == 3):
        sayı1 = random.randint(100,1001)
        sayı2 = random.randint(100,1001)
        cevap = sayı1*sayı2
        islem = "*"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue

    elif(islem_seviye =="Zor" and islem_no == 4):
        sayı1 = random.randint(100,1001)
        sayı2 = random.randint(100,1001)
        cevap = sayı1/sayı2
        islem = "/"
        sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
        if(cevap==sonuc):
            print("Tebrikler!!!")
        else:
            print("Tekrar deneyin!! (Son hakkınız)")
            sonuc = int(input("{}{}{} = ? işleminin sonucu kaçtır?".format(sayı1,islem,sayı2)))
            if(cevap==sonuc):
                print("Tebrikler!!!")
            else:
                print("Cevap yanlış, hakkınız bitmiştir.. Doğru Cevap:",cevap)
        continue
    
    elif(islem_seviye != "Basit" and islem_seviye != "Orta" and islem_seviye != "Zor" and not islem_seviye == "0"):
        print("Zorluk seviyesini yanlış girdiniz! Tekrar deneyin")

    elif(islem_no >= 4):
        print("İşlem numarasını yanlış girdiniz! Tekrar deneyin")
         
    else:
        (islem_seviye == "0" and islem_no == 0)
        print("Oyundan çıkış yapılıyor..")
        print('''İyi günler!
                           (¯`v´¯)
                           `•.¸.•´
                             ☻/
                           / ▌
                            / \ ''')
        break
            
