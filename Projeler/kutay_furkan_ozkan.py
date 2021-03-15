import random

print("     Merhaba, Dört İşlemi Seviyorum oyununa hoşgeldiniz :) Oyunumuzda 4 farklı seviye bulunmaktadır. Bunlar;")
print("     1) Toplama/Çıkarma Bizim İşimiz seviyesinde sayılar 0 ile 10 arasından seçilir ve sadece toplama ile çıkarma işlemleri sorulmaktadır.")
print("     2) Bu İşi Biliyorum seviyesinde sayılar 10 ile 100 arasından seçilir ve toplama, çıkarma ve çarpma işlemleri sorulmaktadır.")
print("     3) Dört İşlem Canavarı seviyesinde sayılar 100 ile 500 arasından seçilir ve dört temel işlem sorulmaktadır. Bölme işleminde sonucun tam kısmı sorulacaktır.")
print("     4) Sayılara Fısıldayan Adam/Kadın seviyesinde ise dört işlem sorulmaktadır. Bölme işleminin sonucu ondalıklı istenmektedir.")
print("     Toplama/Çıkarma Bizim İşimiz seviyesi için 1 yazıp Enter tuşuna basınız")
print("     Bu İşi Biliyorum seviyesi için 2 yazıp Enter tuşuna basınız")
print("     Dört İşlem Canavarı seviyesi için 3 yazıp Enter tuşuna basınız")
print("     Sayılara Fısıldayan Adam/Kadın seviyesi için 4 yazıp Enter tuşuna basınız")
zorluk=int(input("Seçtiğiniz Seviye: "))
operators1=["+","-"]
operators2=["+","-","*"]
operators3=["+","-","*","//"]
operators4=["+","-","*","/"]
operator_functions1 = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
}
operator_functions2 = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}
operator_functions3 = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '//': lambda a, b: a // b,
}
operator_functions4 = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
if zorluk==1:
    sayi1=random.randint(0,10)
    sayi2=random.randint(0,10)
    operator=random.choice(operators1)
    sonuc=operator_functions1[operator](sayi1, sayi2)
    tahmin=int(input("{}{}{}=? işleminin sonucu kaçtır?\n".format(sayi1,operator,sayi2)))
    if sonuc==tahmin:
        print("Bildiniz!")
    else:
        print("Bilemediniz!")
        print("Doğru cevap = {}".format(sonuc))
elif zorluk==2:
    sayi3=random.randint(10,100)
    sayi4=random.randint(10,100)
    operator2=random.choice(operators2)
    sonuc2=operator_functions2[operator2](sayi3, sayi4)
    tahmin2=int(input("{}{}{}=? işleminin sonucu kaçtır?\n".format(sayi3,operator2,sayi4)))
    if sonuc2==tahmin2:
        print("Bildiniz!")
    else:
        print("Bilemediniz!")
        print("Doğru cevap = {}".format(sonuc2))
elif zorluk==3:
    sayi5=random.randint(100,500)
    sayi6=random.randint(100,sayi5)
    operator3=random.choice(operators3)
    sonuc3=operator_functions3[operator3](sayi5, sayi6)
    tahmin3=int(input("{}{}{}=? işleminin sonucu kaçtır?\n".format(sayi5,operator3,sayi6)))
    if sonuc3==tahmin3:
        print("Bildiniz!")
    else:
        print("Bilemediniz!")
        print("Doğru cevap = {}".format(sonuc3))
else:
    sayi7=random.randrange(100,500)
    sayi8=random.randrange(100,sayi7)
    operator4=random.choice(operators4)
    sonuc4=operator_functions4[operator4](sayi7, sayi8)
    tahmin4=input("{}{}{}=? işleminin sonucu kaçtır?\n".format(sayi7,operator4,sayi8))
    if sonuc4==tahmin4:
        print("Bildiniz!")
    else:
        print("Bilemediniz!")
        print("Doğru cevap = {}".format(sonuc4))