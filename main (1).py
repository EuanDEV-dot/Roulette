import time
import random



red = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 29, 31, 33, 35]

even = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

first_dozen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
second_dozen = [0, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
third_dozen = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

money = 1000

gameisrunning = True
while gameisrunning == True:
  start = input('Hello! This is gambling!\nPlease write s for start and q for quit.')
  if start == 's' or start == 'S':
    print('Okay lets go!')
  if start == 'Q' or start == 'q':
    print('Ok BYE')
    break

  print('Du hast', money, '€')
  print('Pick a category to bet on. \n.')


  while money > 0:
    bet = int(input(
        'Pick: \n'
        ' 1 = First or second half (1:1) \n'
        ' 2 = Red or black (1:1) \n'
        ' 3 = Even or odd (1:1) \n'
        ' 4 = First/second7third dozen (2:1) \n'
        ' 5 = Lone numbers (36:1) \n'
    ))
    if bet == 1:
      betierbet1 = int(input('First or second half? \n 1 ='
      'First half (1-18) \n 2 = Second half (19-35)\n'))
      if betierbet1 == 1:
        betmoneyBW11 = int(input('How much money is on the line?'))
        if betmoneyBW11 > money:
          print('You dont have enough money!')
          break
        money = money - betmoneyBW11
        print('Rien ne va plus, thats it!')
        time.sleep(1)
        randomnumber = random.randint(0, 36)
        print('It´s:\n', randomnumber)
        if randomnumber >= 1 and randomnumber <= 19:
          print('You won!')
          money = money + betmoneyBW11 * 2
      if betierbet1 == 2:
        betmoneyBW12 = int(input('How much money is on the line?'))
        if betmoneyBW12 > money:
          print('Your borke pal...')
          break
        money = money - betmoneyBW12
        print('Rien ne va plus, thats it!')
        time.sleep(1)
        randomnumber = random.randint(0, 35)
        print('It´s:\n', randomnumber)
        if randomnumber >= 20 and randomnumber <= 36:
          print('You won!')
          money = money + betmoneyBW12 * 2
    if bet == 2:
      genauewette2 = int(input('Whats it gonna be pal? Red or black?\n 1 = Red\n 2 = Black\n'))
      if genauewette2 == 1:
        wettgeldGW21 = int(input('How much cash is on the line?'))
        if wettgeldGW21 > money:
          print('Bro youre broke!')
          break
        money = money - wettgeldGW21
        print('Rien ne va plus, thats it!')
        time.sleep(1)
        zufallszahl = random.randint(0, 36)
        print('It´s:\n', zufallszahl)
        if zufallszahl in red:
          print('You won!')
          money = money + wettgeldGW21 * 2
      if genauewette2 == 2:
        wettgeldGW22 = int(input('how much cash is on the line?'))
        if wettgeldGW22 > money:
          print('Bro youre broke!')
          break
        money = money - wettgeldGW22
        print('Rien ne va plus, thats it!')
        time.sleep(1)
        zufallszahl = random.randint(0, 36)
        print('Its:\n', zufallszahl)
        if zufallszahl in black:
          print('You won!')
          money = money + wettgeldGW22 * 2
    if bet == 3:
      genauewette3 = int(input('Even or odd?\n1 = Even\n2 = Odd\n'))
      if genauewette3 == 1:
        wettgeldGW31 = int(input('Wie viel möchtest du setzen?'))
        if wettgeldGW31 > money:
          print('Du hast nicht genug Geld')
          break
        geld = money - wettgeldGW31
        print('Rien ne va plus, nichts geht mehr!')
        time.sleep(1)
        zufallszahl = random.randint(0, 36)
        print('Die Nummer die die Kugel entschieden hat ist:\n', zufallszahl)
        if zufallszahl in even:
          print('Du hast won!')
          geld = geld + wettgeldGW31 * 2
      if genauewette3 == 2:
        wettgeldGW32 = int(input('Wie viel möchtest du setzen?'))
        if wettgeldGW32 > money:
          print('You dont have enough money!')
          break
        money = money - wettgeldGW32
        print('Rien ne va plus, nichts geht mehr!')
        time.sleep(1)
        zufallszahl = random.randint(0, 36)
        print('Die Nummer die die Kugel entschieden hat ist:\n', zufallszahl)
        if zufallszahl in odd:
          print('Du hast gewonnen!')
          geld = money + wettgeldGW32 * 2
    if bet == 4:
      genauewette4 = int(input('Willst du auf Erstes, Zweites oder Drittes Dutzend setzten?\n1 = Erstes\n2 = Zweites\n3 = Drittes'))
      if genauewette4 == 1:
        wettgeldGW41 = int(input('Wie viel möchtest du setzen?'))
        if wettgeldGW41 > money:
          print('Du hast nicht genug Geld')
          break
        money = money - wettgeldGW41
        print('Rien ne va plus, nichts geht mehr!')
        time.sleep(1)
        zufallszahl = random.randint(0, 36)
        print('Die Nummer die die Kugel entschieden hat ist:\n', zufallszahl)
        if zufallszahl in first_dozen:
          print('Du hast gewonnen!')
          money = money + wettgeldGW41 * 3
      if genauewette4 == 2:
        wettgeldGW42 = int(input('Wie viel möchtest du setzen?'))
        if wettgeldGW42 > money:
          print('Du hast nicht genug Geld')
          break
        money = money - wettgeldGW42
        print('Rien ne va plus, nichts geht mehr!')
        time.sleep(1)
        zufallszahl = random.randint(0, 36)
        print('Die Nummer die die Kugel entschieden hat ist:\n', zufallszahl)
        if zufallszahl in second_dozen:
          print('Du hast gewonnen!')
          money = money + wettgeldGW42 * 3
      if genauewette4 == 3:
        wettgeldGW43 = int(input('Wie viel möchtest du setzen?'))
        if wettgeldGW43 > money:
          print('Du hast nicht genug Geld')
          break
        money = money - wettgeldGW43
        print('Rien ne va plus, nichts geht mehr!')
        time.sleep(1)
        zufallszahl = random.randint(0, 36)
        print('It´s:\n', zufallszahl)
        if zufallszahl in third_dozen:
          print('Du hast gewon!')
          money = money + wettgeldGW43 * 3
    if bet == 5:
      genauewette5 = int(input('Welche Zahl möchtest du setzen?\n Bitte gib die zahl ein.'))
      wettgeldGW51 = int(input('Wie viel möchtest du setzen?'))
      if wettgeldGW51 > money:
        print('Du hast nicht genug Geld')
        break
      money = money - wettgeldGW51
      print('Rien ne va plus, nichts geht mehr!')
      time.sleep(1)
      zufallszahl = random.randint(0, 36)
      print('Die Nummer die die Kugel entschieden hat ist:\n', zufallszahl)
      if zufallszahl == genauewette5:
        print('Du hast gewonnen!')
        money = money + wettgeldGW51 * 36
    print('Du hast jetzt', money, '€')
    print('\n \n \n')