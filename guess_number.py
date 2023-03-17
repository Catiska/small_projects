from random import *

print('Добро пожаловать в числовую угадайку!')


def is_valid(data):
    return data.isdigit() and 1 <= int(data) <= 10 ** 9


def get_max_num(user_choice):
    if user_choice == 1:
        return 100
    elif user_choice == 2:
        max_num = input('В каком диапазоне играем?\n')
        if not is_valid(max_num):
            print('Введите диапазон цифрами :)')
            return get_game_settings()
        return int(max_num)
    elif user_choice == 3:
        return randint(50, 10000)
    else:
        return get_max_num(user_choice)


def get_game_settings():
    user_choice = input('Ваш выбор: ')
    if not is_valid(user_choice):
        print('Введите выбор режима игры цифрами 1, 2 или 3')
        return get_game_settings()
    return get_max_num(int(user_choice))


def guess_number():
    print('''
Выберите режим игры
1 - стандартный режим (от 1 до 100);
2 - указать свой диапазон (от 1 до 10**9)
3 - игра сама выберет максимальное число
    ''')
    max_num = get_game_settings()
    num = randint(1, max_num)
    print(f'Число загадано в диапазоне от 1 до {max_num}. Попробуйте угадать')
    count = 0
    while True:
        question = input(f'Введите число от 1 до {max_num}:\n')
        if is_valid(question):
            if int(question) > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                count += 1
            elif int(question) < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                count += 1
            elif int(question) == num:
                print(f'Вы угадали, поздравляем!\nВсего попыток: {count}')
                if input('Еще раунд? (y - да; для выхода введи любой '
                         'другой символ)\n').lower() == 'y':
                    guess_number()
                else:
                    print('Спасибо за игру! Еще увидимся! :)')
                    break
                break

def main():
    guess_number()


if __name__ == '__main__':
    main()
  
