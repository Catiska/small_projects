from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
bad_symbols = 'il1Lo0O'


def validate_yes_no(data):
    return data == '1' or data == '2'


def validate_digit(data):
    return data.isdigit()


def validated_data(password_amount,
                   password_len,
                   digit_append,
                   upper_letter_append,
                   lower_letter_append,
                   symbol_append,
                   bad_symbol_delete):
    if (not validate_digit(password_amount)
            or not validate_yes_no(digit_append)
            or not validate_digit(password_len)
            or not validate_yes_no(upper_letter_append)
            or not validate_yes_no(lower_letter_append)
            or not validate_yes_no(symbol_append)
            or not validate_yes_no(bad_symbol_delete)):
        return False
    return True


def get_data():
    password_amount = input(
        'Введите количество паролей для генерации: ')
    password_len = input(
        'Введите длину пароля: ')
    digit_append = input(
        'Добавить цифры в пароль? (1 - да, 2 - нет): ')
    upper_letter_append = input(
        'Добавить прописные буквы в пароль? (1 - да, 2 - нет): ')
    lower_letter_append = input(
        'Добавить строчные буквы в пароль? (1 - да, 2 - нет): ')
    symbol_append = input(
        'Добавить символы в пароль? (1 - да, 2 - нет): ')
    bad_symbol_delete = input(
        'Исключить неоднозначные символы (il1Lo0O)? '
        '(1 - исключить, 2 - оставить): ')
    return (password_amount, password_len, digit_append, upper_letter_append,
            lower_letter_append, symbol_append, bad_symbol_delete)


def password_generate():
    data = get_data()
    if not validated_data(*data):
        print('\n', f'Получены неверные данные - {data}. Вводите ответ '
                    f'числами для длины пароля и количества; 1 - да, 2 - нет '
                    f'для ответов на остальные вопросы.', '\n')
        password_generate()
    password_amount = int(data[0])
    password_len = int(data[1])
    digit_append = data[2]
    upper_letter_append = data[3]
    lower_letter_append = data[4]
    symbol_append = data[5]
    bad_symbol_delete = data[6]

    chars = ''

    if digit_append == '1':
        chars += digits
    if upper_letter_append == '1':
        chars += uppercase_letters
    if lower_letter_append == '1':
        chars += lowercase_letters
    if symbol_append == '1':
        chars += punctuation
    if bad_symbol_delete == '1':
        for symbol in bad_symbols:
            chars = chars.replace(symbol, '')

    if not chars:
        print('Выберите хотя бы одну группу символов.\n')
        return password_generate()

    for char in range(password_amount):
        password = []
        for _ in range(password_len):
            password.append(choice(chars))
        print(''.join(password))


def main():
    password_generate()


if __name__ == '__main__':
    main()
