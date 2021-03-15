import random

levelResult = input("Başlamak için önce bir seviye seçiniz. \nSeviye1 \nSeviye2 \nSeviye3 \n")

operator = [ '+', '-', '/', '*' ]
operatorType = random.choice(operator);

if operatorType == '/':
  print('İşlem sonucunuz ondalıklı sayı ise lütfen virgülden sonra maksimum 2 hane giriniz.')

def switch(operatorType ,num1, num2):
  switcher = {
          '+': num1 + num2,
          '-': num1 - num2,
          '/': num1 / num2,
          '*': num1 * num2,
       }
  return switcher.get(operatorType)

def findResult(level):
  if level == 'Seviye1' or level == 'seviye1' or level =='seviye 1' or level == 'Seviye 1':
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
  elif level == 'Seviye2' or level == 'seviye2' or level == 'seviye 2' or level == 'Seviye 2':
    num1 = random.randint(10, 100)
    num2 = random.randint(10, 100)
  elif level == 'Seviye3' or level == 'seviye3' or level =='seviye 3' or level == 'Seviye 3':
    num1 = random.randint(100, 1000)
    num2 = random.randint(100, 1000)
  else:
    print('Lütfen geçerli bir seçenek giriniz')
    return

  userResult = input("Lütfen {} {} {} işleminin sonucunu giriniz. \n".format(num1, operatorType, num2))

  calcResult = switch(operatorType, num1, num2)
  if "{:10.2f}".format(float(calcResult)) == "{:10.2f}".format(float(userResult)):
    print('Helal')
  else:
    print('Bilemediniz!')
  return
findResult(levelResult)