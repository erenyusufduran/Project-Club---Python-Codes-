# Proje: Bilgisayarın rastgele ürettiği iki sayı ve işlemin sonucunu kullanıcıya soran uygulamayı kodlayınız.

cevap = "e"
while cevap == "e":
    import random

    sayi1 = random.randint(1, 100)
    sayi2 = random.randint(1, 100)
    islem = "+"
    sonuc = sayi1 + sayi2

    cevap = int(input("{}{}{}=? işleminin sonucu kaçtır?".format(sayi1, islem, sayi2)))
    if cevap == sonuc:
        print("Tebrikler bildin!")
    else:
        print("Bilemedin.")

    cevap = input("Tekrardan oynamak ister misiniz? [e]vet / [h]ayır:")