import random



num1 = random.randint(0,100)

num2 = random.randint(0,100)

op = random.randint(0,3)



if(op==0): ## toplama

    result = num1 + num2

    opstr = "+"

elif(op==1): ## cikarma

    result = num1 - num2

    opstr = "-"

elif(op==2): ## carpma

    result = num1 * num2

    opstr = "*"

elif(op==3): ## bolme

    while(1):

        if(num2!=0):

            result = num1/num2

            opstr = ("/")

            break

        else:

            num2 = random.randint(0,100)

        



while(1):

    x = int(input("sonuc tahmini icin bir sayi giriniz: "))

    if ( x > result ):

        print("Daha kucuk bir tahminde bulunun!")

    elif ( x < result ):

        print("Daha buyuk bir tahminde bulunun!")

    else:

        print("Dogru tahmin sayiyi buldunuz Tebrikler!!!!")

        print("Ilk sayinin degeri: " + str(num1) )

        print("Ikinci sayinin degeri: " + str(num2) )

        print("Yapilan islem: " + opstr)

        break
