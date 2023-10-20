#вариант_1

print('Задание №1')

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLACK = '\u001b[40m'
CYAN = '\u001b[46m'
MAGENTA = '\u001b[45m'


def flag_france():
    for _ in range(9):
        print(f'{BLUE}{"  " * 6}{WHITE}{"  " * 6}{RED}{"  " * 6}{END}')

flag_france()
print()

print('Задание №2')

m = int(input('Введите количество повторений узора:'))
def uzor(n):
    for i in range(1, m * 3 + 1):
        if i % 2 == 1:
            print(f'{CYAN}{"  "}{MAGENTA}{"  "}{CYAN}{"  "}{END}')
        elif i % 2 == 0:
            print(f'{MAGENTA}{"  "}{CYAN}{"  "}{MAGENTA}{"  "}{END}')

uzor(m)
print()

print('Задание №3')

print('График функции y = x ** 2')
x = int(input('Введите размер графика, сначала ширину, потом высоту:'))
y = int(input())

print('', '\n')
def graph(m, n): #задаем функцию рисования графика
    for i in range(n, 0, -1): #перебираем значения высоту от большего к меньшему
        if i < 10:          #если число меньше 10, то в нем одна цифра и пробелов надо после него ставить больше
            print(i, end='    ')
        else:               #если число больше или равно 10, то пробелов будет на один меньше, чтобы сохранить красивую сетку графика
            print(i, end='   ')
        for j in range(1, m + 1): #перебираем значения ширины графика от 1 до заданного значения
            if i != j ** 2: #если определенная клетка не соответствует графику, то в ней пишем голубой цвет
                print(f'{CYAN}{"  "}{END}', end="   ") 
            else: #если клетка подходит под график, то пишем красный цвет
                print(f'{RED}{"  "}{END}', end="   ")
        print('\n')    
    for t in range(0, m + 1): #рисуем внизу значения икса
        print(t, end='    ')
graph(x, y)       

print('', '\n')

print('Задание №4 + дополнительное задание')

count_1 = 0
count_2 = 0

lst = [float(x) for x in open("sequence.txt")]

for n in lst:
    if n < 0:
        count_1 += 1
    if n > 0:
        count_2 += 1
print()

import time, sys
def loading():
    print ("Loading..."); time.sleep(3) 
    print('Подсчитываем   количество чисел')
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print
    
loading()
print()
print('Количество чисел меньших нуля равно', count_1)
print('Количество чисел больших нуля равно', count_2)


