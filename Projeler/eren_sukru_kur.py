l1=["+","-"]
l2=["+","-","*"]
l3=[l1,l2]
l_for_b=[20,40,60,80,100]
score=0
import random
while True: 
    level=input("hoşgeldiniz, lütfen, 1 ile 5 arasında ,oynamak istediğiniz zorluk seviyesini giriniz ")
    if int(level) ==1:
          print ("1. zorluk seviyesiyle oynayacaksınız") 
          l=l1
          b=20
          break          
    elif int(level)== 2:
          print("2. zorluk seviyesinde oynayacaksınız")
          l=l1
          b=40
          break
    elif int(level)==3:
          print("3. zorluk seviyesinde oynayacaksınız")
          l=l2
          b=60
          break
    elif int(level)==4:
          print("4. zorluk seviyesinde oynayacaksınız")
          l=l2
          b=80
          break
    elif int(level)==5:
          print("5. zorluk seviyesinde oynayacaksınız")
          l=l2
          b=100
          break  

    else :
        print("girdiğiniz değer geçerli değil, rastgele zorlukta oynayacaksınız ")
        l=random.choice(l3)
        b=random.choice(l_for_b)
        break
while True:
    decision=input("lütfen oyuna devam etmek için devam yazınız, bitirmek için son yazınız ")
    if decision=="devam" :
        first_number=random.randint(1, b)
        second_number=random.randint(1, b)
        operation=random.choice(l)         
        if operation=="+":
            result=first_number+second_number
        elif operation=="-":
            result=first_number-second_number
        elif operation=="*":
                result=first_number*second_number
        while True:
                    ansver=int(input("{}{}{} işleminin sonucu kaçtır, devam etmek istemiyorsanız lütfen 0 tuşlayınız ".format(first_number,operation,second_number)))
                    if ansver==result:
                        print("tebrikler! bildiniz ")
                        score=score+1
                        print("skorunuz {}".format(score))
                        break
                    elif abs(ansver-result)<=2:
                        print("cevaba çok yakınsınız, lütfen işleminizi gözden geçirip yeniden deneyiniz, skorunuzda bir değişme olmayacak")
                    elif ansver==0:
                        print("bu işlem için oyun sonlandırılıyor,son skorunuz {}... ".format(score))
                        break
                    else :
                        print("üzgünüm cevabınız yanlış, lütfen yeniden deneyiniz, çıkmak için 0 yazınız")
                        score=score-1
                        print("maalesef skorunuz bir puan düştü ve {} oldu".format(score))

    elif decision=="son":
        break

    else:
        print("lütfen devam veya son yazınız")
