#Bilgisayarın Rastgele Ürettiği İki Sayı ve İşlemin Sonucunu Kullanıcıya Soran Uygulama

print("Adınızı giriniz")

Ad=input("Adınız:")

print("Oyuna hoşgeldiniz {}.".format(Ad))

print("Zorluk seviyesini seçiniz.")

 

print("Seviye 1 (kolay)")

print("Seviye 2 (orta)")

print("Seviye 3 (zor)")

 

print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

e="evet"

h="hayır"

komut=input("Komut=")

 

sayaç1=0

sayaç2=0

sayaç3=0

sayaç4=0

sayaç5=0

sayaç6=0

 

while komut!="e" and komut!="h":

    print("Yanlış komut girdiniz. Yeniden komut giriniz.")

    print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

    komut=input("Komut=")

 

if komut=="h":

    print("Oyun bitti {}!".format(Ad))

 

while komut=="e" :

zorluk=int(input("Seviye:"))

 

 

while zorluk>3 or zorluk<1  :

    print("Hatalı seviye seçtiniz. Yeniden seviye seçiniz.")

    zorluk=int(input("Seviye:"))

 

print("Oyun başladı {}!".format(Ad))

 

 

 

 

 

from random import randint

 

 

 

 

 

if zorluk==1:

    sayı1=randint(1,100)

    sayı2=randint(1,100)

    print("sayı1=",sayı1)

    print("sayı2=",sayı2)

 

    if sayı1<50:

        işlem="-"

        sonuç=sayı1-sayı2

 

    else :

        işlem="+"

        sonuç=sayı1+sayı2

 

    print("sonuç=sayı1{}sayı2".format(işlem))

    cevap=int(input("sonuç="))

 

   

    if cevap==sonuç:

        print("Tebrikler {}, bildiniz".format(Ad))

        print("+10 puan")

        sayaç1+=1

        print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

        e="evet"

        h="hayır"

        komut=input("Komut=")

 

        while komut!="e" and komut!="h":

          print("Yanlış komut girdiniz. Yeniden komut giriniz.")

          print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

          komut=input("Komut=")

 

        if komut=="h":

          print("Oyun bitti {}!".format(Ad))

       

 

 

       

    else :

        print("Üzgünüm {}, bilemediniz. Doğru cevap=".format(Ad),sonuç)

        print("-5 puan")

        sayaç2+=1

 

        print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

        e="evet"

        h="hayır"

        komut=input("Komut=")

 

        while komut!="e" and komut!="h":

         print("Yanlış komut girdiniz. Yeniden komut giriniz.")

         print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

         komut=input("Komut=")

 

        if komut=="h":

         print("Oyun bitti {}!".format(Ad))

 

      

 

 

 

if zorluk==2:

    sayı1=randint(1,100)

    sayı2=randint(1,100)

    print("sayı1=",sayı1)

    print("sayı2=",sayı2)

 

    if sayı1<50:

        işlem="*"

        sonuç=sayı1*sayı2

 

    else :

        işlem="//"

        sonuç=sayı1//sayı2

        print("Sonucun tam kısmını yazmanız yeterlidir.")

 

    print("sonuç=sayı1{}sayı2".format(işlem))

    cevap=int(input("sonuç="))

 

   

    if cevap==sonuç:

        print("Tebrikler {}, bildiniz".format(Ad))

        print("+20 puan")

        sayaç3 += 1

        print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

        e="evet"

        h="hayır"

        komut=input("Komut=")

 

        while komut!="e" and komut!="h":

         print("Yanlış komut girdiniz. Yeniden komut giriniz.")

         print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

         komut=input("Komut=")

 

        if komut=="h":

         print("Oyun bitti {}!".format(Ad))

 

 

 

 

  

    else :

        print("Üzgünüm {}, bilemediniz. Doğru cevap=".format(Ad),sonuç)

        print("-10 puan")

        sayaç4+=1

 

        print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

        e="evet"

        h="hayır"

        komut=input("Komut=")

 

        while komut!="e" and komut!="h":

         print("Yanlış komut girdiniz. Yeniden komut giriniz.")

         print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

         komut=input("Komut=")

 

        if komut=="h":

         print("Oyun bitti {}!".format(Ad))

 

 

 

 

 

if zorluk==3:

    sayı1=randint(100,1000)

    sayı2=randint(100,1000)

    print("sayı1=",sayı1)

    print("sayı2=",sayı2)

 

 

    if sayı1<50:

        işlem="-"

        sonuç=sayı1-sayı2

 

    if sayı1>49 and sayı1<100 :

        işlem="+"

        sonuç=sayı1+sayı2

 

    if sayı1>99 and sayı1<500:

        işlem="*"

        sonuç=sayı1*sayı2

 

    if sayı1>499 and sayı1<1001:

        işlem="//"

        sonuç=sayı1//sayı2

        print("Sonucun tam kısmını yazmanız yeterlidir.")

 


    print("sonuç=sayı1{}sayı2".format(işlem))

    cevap=int(input("sonuç="))

 

   

    if cevap==sonuç:

        print("Tebrikler {}, bildiniz".format(Ad))

        print("+30 puan")

        sayaç5+=1

 

        print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

        e="evet"

        h="hayır"

        komut=input("Komut=")

 

        while komut!="e" and komut!="h":

         print("Yanlış komut girdiniz. Yeniden komut giriniz.")

         print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

         komut=input("Komut=")

 

        if komut=="h":

         print("Oyun bitti {}!".format(Ad))

 

 

 

  

 

    else :

        print("Üzgünüm {}, bilemediniz. Doğru cevap=".format(Ad),sonuç)

        print("-15 puan")

        sayaç6+=1

 

        print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

        e="evet"

        h="hayır"

        komut=input("Komut=")

 

        while komut!="e" and komut!="h":

         print("Yanlış komut girdiniz. Yeniden komut giriniz.")

         print("Oyuna başlamak veya devam etmek için 'e' tuşuna basınız. Oyunu bitirmek için 'h' tuşuna basınız.")

         komut=input("Komut=")

 

        if komut=="h":

         print("Oyun bitti {}!".format(Ad))

 

 

ToplamPuan = (sayaç1*(10)) + (sayaç2*(-5)) + (sayaç3*(20)) + (sayaç4*(-10)) + (sayaç5*(30)) + (sayaç6*(-15))

print("Toplam puanınız=",ToplamPuan)

...
