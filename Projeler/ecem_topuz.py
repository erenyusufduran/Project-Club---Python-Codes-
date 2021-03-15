input("---VÜCUT KİTLE ENDEKSİ HESAPLAMA SİSTEMİNE HOŞGELDİNİZ!---")

import random
ad = input("ADINIZ NEDİR? :")
kilo = float(input("KİLONUZ KAÇ? :"))
boy = float(input("BOYUNUZ KAÇ?(m cinsinden belirtiniz) :"))

index = (kilo/(boy**2))

if (index >= 0) and (index <= 18.4) :
  print("İDEAL KİLONUZUN ALTINDASINIZ. KİLO ALMANIZ TAVSİYE OLUNUR.")
elif (index > 18.4) and (index <= 24.9) :
  print("İDEAL KİLODASINIZ.")
elif (index > 24.9) and (index <= 29.9) :
  print("İDEAL KİLONUZUN ÜZERİNDESİNİZ. KİLO VERMENİZ TAVSİYE OLUNUR.")
elif (index >29.9) and (index <=34.9 ) :
   print("İDEAL KİLONUZUN ÇOK ÜZERİNDESİNİZ. BİR SAĞLIK KURULUŞUNA GİTMENİZ TAVSİYE OLUNUR.")
