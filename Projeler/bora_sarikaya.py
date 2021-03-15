import random
def islem(sayi1,sayi2,op):
    if op=="*":
        cevap=sayi1*sayi2
    elif op=="+":
        cevap=sayi1+sayi2
    elif op=="-":
        cevap=sayi1-sayi2
    elif op=="/":
        cevap=round(sayi1/sayi2,1)
        if sayi1%sayi2==0:
            cevap=int(cevap)
    return cevap
while True:
    print("Hesap oyununa hoşgeldin. Burda işler şöyle yürüyor:\n1)Oyun esnasında size 2 adet sayı ve bir adet işlem operatörü verilecek.\n2)Doğru sonucu bilemezseniz yeni soru verilecek.\n3)Oyun esnasında bir önceki menüye dönmek için 'g' tuşuna basmanız gerekmektedir")
    nE=input("\n\nŞimdi ne yapmak istersiniz?\n1)Uygulamadan çıkış.\n2)Programcıyı tanımak :)\n3)Oyuna başla\n")
    if nE=="3":
        print("\nZORLUK DERECENİZİ SEÇİNİZ(1-2-3):")
        x=int(input("\n1)Başlangıç\n2)Orta seviye\n3)Şampiyon\n"))
        while True:
            sayi1=random.randint(1,x*35)
            sayi2=random.randint(1,x*35)
            o=["*","/","+","-"]
            op=random.choice(o)
            cevap=islem(sayi1,sayi2,op)
            print("****************************************\n")
            print(str(sayi1)+op+str(sayi2))
            resp=str(input("Cevabınız nedir?\n"))
            if(resp==str(cevap)):
                print("...Tebrikler Bildiniz...\n")
            elif(resp=="g"):
                print("Önceki menüye dönülüyor...\n")
                break
            else:
                print("Bilemediniz :(\n")
                print(cevap)
    elif nE=="1":
        break
    elif nE=="2":
        print("Öncelikle bu seçeneği seçtiğin için teşekkür ederim.\n\nBen Bora SARIKAYA, ODTÜ 1. sınıf Elektrik Elektronik Mühendisliği öğrencisiyim.\n2019 yılında METU Formula Racing topluluğunda elektronik takım üyeliğiyle beraber kodlamayla tanıştım.\n")
        print("Daha sonra öğrencilerinizden birisi olan Berkay Türk ile ortak projemiz olan 'jarvis' üzerine çalışmaya başladık.\nKendisi machine learning özelliklerine sahip bir yapay zeka sesli asistan.\n")
        print("Hala jarvis üzerinde çalışmakla beraber ODTÜ Robot Topluluğunda robotik takımındayım ayrıca bir IHA takımı olan METUrone un elektronik takım üyesiyim.\nLinkedin hesabımı geliştirmek istiyorum. Takip ederseniz çok sevinirim.\nİŞLEMLER başlığı altında iletişim bilgilerim bulunmakta.\nTeşekkür ederim.\n")
        while True:
            
            z=int(input("\nİŞLEMLER(1-2-3-4):\n1)İLETİŞİM BİLGİLERİ.\n2)EVET BORA SENİ İSTANBUL'A DAVET ETMEK İSTERİZ.\n3)EVET TAM SENLİK BİR STAJIMIZ VAR.\n4)çıkış :(\n"))
            if z==1:
                print("\nE-mail: boras916@gmail.com\nİnstagram: boras58\nLinkedin: https://www.linkedin.com/in/bora-sarikaya-78712619a")
            elif z==2:
                print("\nHer türlü teknoloji, bilim festival ve konferanslarınıza katılmak isterim.\nDavet ederseniz çok mutlu olurum. Mail atabilirsiniz.")
            elif z==3:
                print("\nboras916@gmail.com")
            elif z==4:
                break
            else:print("\nöyle bir seçeneğimiz yok mahalesef\n")

    
        
        