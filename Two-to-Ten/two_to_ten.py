import random


print(" " * 28 + "TWO TO TEN")
print(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN NEW JERSEY")
print()
print()
print()
print("WELCOME TO THE GAME OF TWO TO TEN.  THAT NAME COMES FROM THE")
print("SPECIAL 'DECK OF CARDS' USED. THERE ARE NO FACE CARDS - ONLY")
print("THE CARDS 2-10.  THIS GAME IS EASY AND FUN TO PLAY IF YOU")
print("UNDERSTAND WHAT YOU ARE DOING SO READ THE INSTRUCTIONS")
print("CAREFULLY.")
print("AT THE START OF THE GAME, YOU BET ON WINNING. TYPE IN ANY")
print("NUMBER BETWEEN 0 AND 200.  I THEN PICK A RANDOM NUMBER")
print("YOU ARE TO REACH BY THE SUM TOTAL OF MORE CARDS CHOSEN.")
print("BECAUSE OF THE RARE CHANCE OF YOU GETTING TO THAT NUMBER")
print("EXACTLY, YOU ARE GIVEN AN ALLOWANCE CARD.  THE OBJECT OF")
print("THE GAME OF TO GET THE TOTAL OF CARDS WITHIN THE MYSTERY")
print("NUMBER WITHOUT GOING OVER.")
print("YOU ARE GIVEN A HINT AS TO WHAT THE NUMBER IS.  THIS IS NOT")
print("THE EXACT NUMBER ONLY ONE CLOSE. ALL YOU DO IN THIS GAME IS")
print("DECIDE WHEN TO STOP.  AT THIS POINT YOUR TOTAL IS COMPARED")
print("WITH THE NUMBER AND YOUR WINNINGS ARE DETERMINED.")

# Инициализация переменных
M = 200  # Деньги игрока
D = 0    # Счетчик карт
T = 0    # Общая сумма выбранных карт

# Генерация случайных чисел для установки параметров игры
O = random.randint(25, 34)
N = random.randint(O, O * 2)
R = (random.randint(1, 15) / 100)
S = random.randint(1, 2)

# Вычисление значения E в зависимости от S
if S != 1:
    E = int(N - (N * R))
else:
    E = int(N + (N * R))

# Генерация случайного числа A для "лимита удачи"
A = random.randint(2, 10)

# Запрос ставки от игрока и проверка ее корректности
print()
print(f"PLACE YOUR BET ... YOU HAVE ${M} TO SPEND.")
B = int(input())
print()

if B < 0:
    print("YOU CAN'T BET MORE THAN YOU'VE GOT!")
elif M < B:
    print("YOU CAN'T BET MORE THAN YOU HAVE!")
else:
    # Вывод информации о "лимите удачи"
    print(f"YOUR 'LUCKY LIMIT' CARD IS A {A}")
    print(f"YOU MUST COME WITHIN {A} WITHOUT GOING OVER TO WIN.")
    print()
    print("HERE WE GO")
    print()
    print()

    while True:
        # Игроку раздаются карты и выводится информация о них
        D += 1
        C = random.randint(2, 10)
        print(f"CARD #{D} IS A {C}. YOU ARE TRYING TO COME NEAR {E}")
        T += C

        # Проверка, не превышает ли общая сумма (T) загаданное число (N)
        if T > N:
            print(f"YOUR TOTAL IS OVER THE NUMBER {N} - AN AUTOMATIC LOSS!")
            break

        # Хочет ли игрок продолжать
        print(f"YOUR TOTAL IS {T}. DO YOU WANT TO CONTINUE?")
        Q = input()
        print()

        if Q.lower().startswith('y'):
            continue

        # Проверка условий выигрыша или проигрыша
        if T < N - A or T > N:
            print(f"YOU BLEW IT! THE NUMBER WAS {N}, OUTSIDE YOUR LIMIT BY {abs(N - A - T)}")
            print()
            M -= B
        else:
            print(f"YOU WIN! THE NUMBER WAS {N}, YOUR GUESS TOTAL WAS {T} WITHIN YOUR LIMIT CARD.")
            M += B

        # Вывод информации о деньгах и проверка на банкротство
        print(f"YOU NOW HAVE ${M} IN CASH TO BET IN THE NEXT GAME!")

        if M <= 0:
            print()
            print(chr(7))
            print("YOU ARE BROKE!! YOU MAY NOT PLAY ANYMORE!!")
            break

        # Хочет ли игрок начать следующую игру
        print("WOULD YOU LIKE TO PLAY THE NEXT GAME?")
        Q = input()

        if not Q.lower().startswith('y'):
            print("HOPE YOU HAD FUN.")
            break
