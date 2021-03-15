import random
sayi1=random.randrange(0,50)
sayi2=random.randrange(0,50)
işlemlst=["+","-","//","*"]
işlemler=random.choice(işlemlst)
sonuc=sayi1,random.sample(işlemler,1),sayi2


cevap=int(input("{}{}{}=? işleminin sonucu kaçtır ?".format(sayi1,işlemler,sayi2)))

if cevap==sonuc:
    print("bildin")
else:
    print("bilemedin")