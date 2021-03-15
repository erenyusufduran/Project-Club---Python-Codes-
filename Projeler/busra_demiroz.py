print("Hoşgeldiniz!")
print("1 : Toplama")
print("2 : Çıkarma")
print("3 : Çarpma")
print("4 : Bölme")

import random
sayi1 = random.randint(1,100)
sayi2 = random.randint(1,100)

i = 1
while i == 1:
  soru = input("Hangi işlemi yapmak istersiniz: ")
  if soru == "1":
    islem = "+"
  elif soru == "2":
    islem = "-"
  elif soru == "3":
    islem = "*"
  else:
    islem = "//"
  break

if islem == "+":
  sonuc = sayi1 + sayi2
elif islem == "-":
  sonuc = sayi1 - sayi2
elif islem == "*":
  sonuc = sayi1 * sayi2
else:
  sonuc = sayi1 // sayi2

while 5 == 5:
 cevap = int(input("{} {} {} sonucu kaçtır? ".format(sayi1,islem,sayi2)))
 if cevap == sonuc :
   print("Tebrikler Bildiniz!")
   break
 else:
   print("Bilemediniz. Lütfen yeni bir değer giriniz:")

