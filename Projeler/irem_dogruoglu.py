import random

print('İşlem sonucunu tahmin etme oyununa hoşgeldiniz!')
print('Zorluk seviyesini seçiniz:')
print('1. seviye')
print('2. seviye')
print('3. seviye')
zorluk=input('Seçiniz:')

liste=['toplama','çıkarma','çarpma','bölme','üs alma']
seçim= random.choice(liste)

sayı1 = random.randint(0, 100)
sayı2 = random.randint(0, 100)


if seçim == 'toplama':
    cevap=sayı1 + sayı2
    soru= int(input('{}{}{}=? işleminin sonucu kaçtır?'.format(sayı1,'+',sayı2)))
    if cevap == soru:
        print('Tebrikler, bildiniz!')
    else:
        print('Bilemediniz!')

elif seçim == 'çıkarma':
    cevap=sayı1 - sayı2
    soru= int(input('{}{}{}=? işleminin sonucu kaçtır?'.format(sayı1,'-',sayı2)))
    if cevap == soru:
        print('Tebrikler, bildiniz!')
    else:
        print('Bilemediniz!')

elif seçim == 'çarpma':
    cevap=sayı1 * sayı2
    soru= int(input('{}{}{}=? işleminin sonucu kaçtır?'.format(sayı1,'*',sayı2)))
    if cevap == soru:
        print('Tebrikler, bildiniz!')
    else:
        print('Bilemediniz!')

elif seçim == 'bölme':
    cevap=sayı1 / sayı2
    soru= int(input('{}{}{}=? işleminin sonucu kaçtır?'.format(sayı1,'/',sayı2)))
    if cevap == soru:
        print('Tebrikler, bildiniz!')
    else:
        print('Bilemediniz!')

elif seçim == 'üs alma':
    cevap=sayı1 ** sayı2
    soru= int(input('{}{}{}=? işleminin sonucu kaçtır?'.format(sayı1,'**',sayı2)))
    if cevap == soru:
        print('Tebrikler, bildiniz!')
    else:
        print('Bilemediniz!')
else:
    print('Lütfen tekrar deneyiniz!')