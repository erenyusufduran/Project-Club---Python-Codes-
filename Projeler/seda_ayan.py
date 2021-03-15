# ------------------------------------------------------------------------------------------------
# ---------------------------------- Sihirli Sayılar  Oyunu ----------------------------------
# ------------ Kurallar ------------
# -- Oyunumuza isminizi öğrenerek başlıyoruz ve ardından siz hazır olana kadar oyuna başlamak için sabırsızlıkla bekliyoruz. --
# -- Daha sonra birinci sayınız için bir zorluk derecesi belirlemenizi istiyoruz, seçilen zorluk seviyesinin 10 katı puan kazanarak oyuna başlıyorsunuz. --
# -- Seçtiğiniz zorluk seviyesinin değer aralığında 1.sayınızı  bulmanız gerekmektedir, her yeni sayı denemenizde zorluk seviyeniz kadar puan kaybedersiniz. --
# -- 1.Sayınızı bulununca sayıyı aklınızda tutmanız gerekmektedir. Daha sonra 2.Sayı bulma bölümüne geçilir ve aynı kurallar burada da gecerli olur. --
# -- Oyunumuza Hesaplamaca kısmıyla devam ederiz ve aklınızda tuttuğunuz 2 sayı ile herhangi bir işlem yapmanız istenir. Bunu işlem sonucunu doğru bildiğinizde puanınıza +50 eklenir. --
# -- Oyun sona erer ve puanlama tablosu oluşur, oyuna devam etmek isteyen oyuncular oyun sonunda gelen soru ile tekrar oynayıp kendi rekorunu gecebilir. --
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Seda Nur Ayan  ( ssedaayann@gmail.com )


import time
import random

my_list = []
puan = 0
num = 0


def my_func():
    print('Lütfen tekrar deneyiniz')
    global num
    num = int(input())
    global puan
    puan = puan - 5


name = (input(' Hoş geldiniz, isminiz nedir?'))
oyun = (input('Merhaba ' + str(
    name) + ' , Sihirli Sayılar oyunumuza hoş geldin :) Oyunumuza başlamaya hazır mısın? (Evet, Hayır) '))
loop = True
while loop:
    puan = 0
    while 1:
        if oyun.lower() == 'evet':
            break
        elif oyun.lower() == 'hayır':
            time.sleep(1)
            print('Peki seni sabırsızlıkla bekliyorum ' + str(name))
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            print('Şimdi hazır mısın?')
            oyun = input()
        else:
            print('Yazım yanlışlarına dikkat etmelisin ' + str(name) + ' :) Haydi tekrar dene Evet mi Hayır mı? ')
            oyun = input()
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print('Veee Başlıyoruz')
    time.sleep(1)

    print(
        'Lütfen birinci sayı için oynamak istediğiniz zorluk seviyesini seçiniz: 1. Seviye = (1, 50); 2. Seviye = (1, 100); 3. Seviye = (1, 150), (1, 2 ya da 3 yazman yeterli). Seçtiğiniz seviyenin 10 katı kadar puan kazanarak oyuna başlarsın.')
    while 1:
        x = int(input())
        if x in [1, 2, 3]:
            break
        else:
            print('Sadece birinci, ikinci ve üçüncü seviyelerden seçim yapabilirsin ' + str(
                name) + '. (1, 2 ya da 3 yazmalısın)')
    x1num = random.randint(1, 50 * x)
    num = int(input('Lütfen 1 ile ' + str(
        50 * x) + ' arasında bir sayı giriniz. Unutma her yanlış denemende seçili seviyen kadar puan kaybedersin.'))
    while num != x1num:
        if num < x1num:
            print(f'{num} dan daha büyük bir sayı girmelisin')
            num = int(input())
        elif num >= 50 * x:
            print('Lütfen 1 ile ' + str(50 * x) + ' arasında bir sayı giriniz')
            num = int(input())
        else:
            print(f'{num} dan daha küçük bir sayı girmelisin.')
            num = int(input())
        puan = puan - x
    print('Tebrikler ' + str(name) + f' {num} sayısını buldunuz, ilk sayını aklında tut ve ikinci sayını bul! ')
    puan = puan + 10 * x

    time.sleep(1)
    xx = x
    print(
        'Lütfen ikinci sayı için oynamak istediğiniz zorluk seviyesini seçiniz: 1. Seviye = (1, 50); 2. Seviye = (1, 100); 3. Seviye = (1, 150), (1, 2 ya da 3 yazman yeterli). Seçtiğiniz seviyenin 10 katı kadar puan kazanarak oyuna devam edersiniz.')
    while 1:
        x = int(input())
        if x in [1, 2, 3]:
            break
        else:
            print('Sadece birinci, ikinci ve üçüncü seviyelerden seçim yapabilirsin ' + str(
                name) + '. (1, 2 ya da 3 yazmalısın)')
    x2num = random.randint(1, 50 * x)
    num = int(input('Lütfen 1 ile ' + str(
        50 * x) + ' arasında bir sayı giriniz. Unutma her yanlış denemende seçili seviyen kadar puan kaybedersin.'))
    while num != x2num:
        if num < x2num:
            print(f'{num} dan daha büyük bir sayı girmelisin')
            num = int(input())
        elif num >= 50 * x:
            print('Lütfen 1 ile ' + str(50 * x) + ' arasında bir sayı giriniz')
            num = int(input())
        else:
            print(f'{num} dan daha küçük bir sayı girmelisin.')
            num = int(input())
        puan = puan - x
    print(f' Tebrikler ' + str(
        name) + ' sayıları bulma işlemini başarıyla tamamladın, sayılarını aklında tutmaya devam et. Şimdi oyunumuzun ikinci kısmı olan Hesaplamaca ya geçiş yapıyoruz.')
    puan = puan + 10 * x

    time.sleep(1)
    ihtimal = random.randint(1, 7)
    if ihtimal == 1:
        print('Birinci sayın ile ikinci sayının toplamı kaçtır?')
        num = int(input())
        while 1:
            result = x1num + x2num
            if num == x1num + x2num:
                break
            else:
                my_func()
    elif ihtimal == 2:
        print('Birinci sayından ikinci sayını mutlak değerli olarak çıkarttığında sonuç kaç olur?')
        num = int(input())
        while 1:
            result = abs(x1num - x2num)
            if num == abs(x1num - x2num):
                break
            else:
                my_func()
    elif ihtimal == 3:
        print(' Birinci sayın ile ikinci sayının  çarpımı kaçtır?')
        num = int(input())
        while 1:
            result = x1num * x2num
            if num == x1num * x2num:
                break
            else:
                my_func()
    elif ihtimal == 4:
        print('Birinci sayı + ikinci sayı * 2 işleminin sonucu kaç olur?')
        num = int(input())
        while 1:
            result = x1num + x2num * 2
            if num == x1num + x2num * 2:
                break
            else:
                my_func()

    elif ihtimal == 5:
        print('Birinci sayıyı ikinci sayıyla çarpıp  5 ekleyiniz')
        num = int(input())
        while 1:
            result = (x1num * x2num) + 5
            if num == (x1num * x2num) + 5:
                break
            else:
                my_func()
    elif ihtimal == 6:
        print('Birinci sayının karesi kaç olur?')
        num = int(input())
        while 1:
            result = x1num ** 2
            if num == x1num ** 2:
                break
            else:
                my_func()
    elif ihtimal == 7:
        print('İkinci sayının küpü kaç olur?')
        num = int(input())
        while 1:
            result = x2num ** 3
            if num == x2num ** 3:
                break
            else:
                my_func()

    puan = puan + 50
    print(' Tebrikler toplam puanınız ' + str(puan))
    my_list.append(puan)
    print(my_list)

    print('Oyunumuzun sonuna geldik ' + str(name) + '. Tekrar oynayıp kendi rekorunu geçmek ister misin? ')
    while 1:
        result = input()
        if result.lower() == 'evet':
            print('Yaşasın!! Devam ediyoruz')
            time.sleep(1)
            oyun = (input(' ' + str(
                name) + ', Sihirli Sayılar oyunumuza tekrar hoş geldin :) Oyunumuza başlamaya hazır mısın? (Evet, Hayır) '))
            break
        elif result.lower() == 'hayır':
            loop = False
            break
        else:
            print('Yazım yanlışlarına dikkat etmelisin ' + str(name) + '. Evet mi Hayır mı?')

print('Katıldığın için teşşekkür ederiz, tekrar görüşmek üzere ' + str(name) + ' :) Puan tablonuzun son hali ' + str(
    my_list) + '. Tebrikler.')