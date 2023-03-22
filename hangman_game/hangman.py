from random import choice
from hangman_settings import word_list, display_hangman


def get_word():
    return choice(word_list).upper()


def play(attempt, word, word_completion):
    while attempt > 0:
        word_completion = list(word_completion)
        answer = input('Введите одну букву: ').upper()
        if len(answer) > 1:
            print('Введите только одну букву.')
            continue
        if answer not in word:
            print(display_hangman(attempt - 1))
            print(f'Нет такой буквы. Осталось попыток - {attempt - 1}')
            attempt -= 1
        for index, letter in enumerate(word):
            if answer == letter:
                word_completion[index] = answer
        print(''.join(word_completion))
        if ''.join(word_completion) == word:
            print('Верно! Вы выиграли!')
            break
        if attempt == 0:
            print(f'Вы проиграли. Загаданное слово - {word}.')


def main():
    word = get_word()
    attempt = 6
    word_completion = '_' * len(word)
    print(f'Загадано слово {word_completion}')
    print(display_hangman(attempt))
    play(attempt, word, word_completion)


if __name__ == '__main__':
    main()
