import random

liste = ["*", "-", "+", "/"]

devam = True
puan = 0

while (devam == True):
    sayi1 = random.randint(1, 100)
    sayi2 = random.randint(1, 100)
    islem = random.choice(liste)
    print("{} {} {} = ".format(sayi1, islem, sayi2))
    yanit = int(input())
    if (islem == "*"):
        cevap = sayi1 * sayi2
    elif (islem == "-"):
        cevap = sayi1 - sayi2
    elif (islem == "+"):
        cevap = sayi1 + sayi2
    elif (islem == "/"):
        cevap = int(sayi1 / sayi2)

    if (cevap == yanit):
        print("Bildiniz!")
        puan = puan + 5
    else:
        print("Bilemediniz!")
        print("Puanınız= {}".format(puan))
        devam = False