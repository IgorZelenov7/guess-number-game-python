from random import randint

print('Добро пожаловать в игру "Числовая угадайка"!')
q = int(input('Введите крайнюю правую границу числовой последовательности: '))
x = randint(1, q)


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= q


def repeat_input():
    while True:
        n = input(f'Введите целое число от 1 до {q}: ')
        if is_valid(n):
            return int(n)
        else:
            print(f'Ошибка! Введите целое цисло от 1 до {q} ')


def play_game():
    cnt = 0

    while True:
        n = repeat_input()
        if n < x:
            cnt += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > x:
            cnt += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', cnt)
            if repeat_game():
                continue
            else:
                break


def repeat_game():  
    while True:
        s = input('Хотите сыграть еще раз? (да/нет): ')
        if s.lower() in 'ада':
            return True
        if s.lower() in 'енетент':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')   
            return False
        else:
            print('Ошибка ввода! Принимаемые ответы только "да" или "нет"')    


play_game()
