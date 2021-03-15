import random



sayi1 = random.randint(0,100)

sayi2 = random.randint(0,100)

islem = random.randint(0,3)



if(islem==0): ## toplama

    sonuc = sayi1 + sayi2

    islemstr = "+"

elif(islem==1): ## cikarma

    sonuc = sayi1 - sayi2

    islemstr = "-"

elif(islem==2): ## carpma

    sonuc = sayi1 * sayi2

    islemstr = "*"

elif(islem==3): ## bolme

    while(1):

        if(sayi2!=0):

            sonuc = sayi1/sayi2

            islemstr = ("/")

            break

        else:

            sayi2 = random.randint(0,100)

        



while(1):

    x = int(input("sonucun tahmini icin bir sayi giriniz: "))

    if ( x > sonuc ):

        print("Daha kucuk bir tahminde bulunun!")

    elif ( x < sonuc ):

        print("Daha buyuk bir tahminde bulunun!")

    else:

        print("Dogru tahmin sayiyi buldunuz Tebrikler!")

        print("Ilk sayinin degeri: " + str(sayi1) )

        print("Ikinci sayinin degeri: " + str(sayi2) )

        print("Yapilan islem: " + islemstr)

        break

