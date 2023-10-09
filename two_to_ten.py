import random


def is_web():
    return "__BRYTHON__" in globals()

def write(message, end='\n'):
    if is_web():
        from browser import document
        console = document.getElementById('console')
        p = document.createElement('p')
        p.textContent = '> ' + message
        console.appendChild(p)
        console.scrollTop = console.scrollHeight
    else:
        print(message, end=end)


async def read():
    if is_web():
        from browser import document, aio
        inp = document.getElementById('input')
        while True:
            event = await aio.event(inp, 'keydown')
            if event.key == 'Enter':
                tmp = event.target.value
                event.target.value = ''
                write(tmp)
                return tmp
    else:
        return input()


def run(function):
    if is_web():
        from browser import aio
        aio.run(function())
    else:
        import asyncio
        asyncio.run(function())


async def two_to_ten():
    write(" " * 28 + "TWO TO TEN")
    write(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN NEW JERSEY")
    write('')
    write('')
    write('')
    write("WELCOME TO THE GAME OF TWO TO TEN.  THAT NAME COMES FROM THE")
    write("SPECIAL 'DECK OF CARDS' USED. THERE ARE NO FACE CARDS - ONLY")
    write("THE CARDS 2-10.  THIS GAME IS EASY AND FUN TO PLAY IF YOU")
    write("UNDERSTAND WHAT YOU ARE DOING SO READ THE INSTRUCTIONS")
    write("CAREFULLY.")
    write("AT THE START OF THE GAME, YOU BET ON WINNING. TYPE IN ANY")
    write("NUMBER BETWEEN 0 AND 200.  I THEN PICK A RANDOM NUMBER")
    write("YOU ARE TO REACH BY THE SUM TOTAL OF MORE CARDS CHOSEN.")
    write("BECAUSE OF THE RARE CHANCE OF YOU GETTING TO THAT NUMBER")
    write("EXACTLY, YOU ARE GIVEN AN ALLOWANCE CARD.  THE OBJECT OF")
    write("THE GAME OF TO GET THE TOTAL OF CARDS WITHIN THE MYSTERY")
    write("NUMBER WITHOUT GOING OVER.")
    write("YOU ARE GIVEN A HINT AS TO WHAT THE NUMBER IS.  THIS IS NOT")
    write("THE EXACT NUMBER ONLY ONE CLOSE. ALL YOU DO IN THIS GAME IS")
    write("DECIDE WHEN TO STOP.  AT THIS POINT YOUR TOTAL IS COMPARED")
    write("WITH THE NUMBER AND YOUR WINNINGS ARE DETERMINED.")

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
    write('')
    write(f"PLACE YOUR BET ... YOU HAVE ${M} TO SPEND.")
    B = int(await read())
    write('\n')

    if B < 0:
        write("YOU CAN'T BET MORE THAN YOU'VE GOT!")
    elif M < B:
        write("YOU CAN'T BET MORE THAN YOU HAVE!")
    else:
        # Вывод информации о "лимите удачи"
        write(f"YOUR 'LUCKY LIMIT' CARD IS A {A}")
        write(f"YOU MUST COME WITHIN {A} WITHOUT GOING OVER TO WIN.")
        write('')
        write("HERE WE GO")
        write('')
        write('')

        while True:
            # Игроку раздаются карты и выводится информация о них
            D += 1
            C = random.randint(2, 10)
            write(f"CARD #{D} IS A {C}. YOU ARE TRYING TO COME NEAR {E}")
            T += C

            # Проверка, не превышает ли общая сумма (T) загаданное число (N)
            if T > N:
                write(f"YOUR TOTAL IS OVER THE NUMBER {N} - AN AUTOMATIC LOSS!")
                break

            # Хочет ли игрок продолжать
            write(f"YOUR TOTAL IS {T}. DO YOU WANT TO CONTINUE?")
            Q = await read()
            write('')

            if Q.lower().startswith('y'):
                continue

            # Проверка условий выигрыша или проигрыша
            if T < N - A or T > N:
                write(f"YOU BLEW IT! THE NUMBER WAS {N}, OUTSIDE YOUR LIMIT BY {abs(N - A - T)}")
                write('')
                M -= B
            else:
                write(f"YOU WIN! THE NUMBER WAS {N}, YOUR GUESS TOTAL WAS {T} WITHIN YOUR LIMIT CARD.")
                M += B

            # Вывод информации о деньгах и проверка на банкротство
            write(f"YOU NOW HAVE ${M} IN CASH TO BET IN THE NEXT GAME!")

            if M <= 0:
                write("")
                write(chr(7))
                write("YOU ARE BROKE!! YOU MAY NOT PLAY ANYMORE!!")
                break

            # Хочет ли игрок начать следующую игру
            write("WOULD YOU LIKE TO PLAY THE NEXT GAME?")
            Q = await read()

            if not Q.lower().startswith('y'):
                write("HOPE YOU HAD FUN.")
                break

run(two_to_ten)
