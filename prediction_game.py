from random import choice

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да',
           'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего',
           'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже',
           'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай',
           'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как Вас зовут?\n')
print(f'Привет, {name}')


def prediction_game():
    while True:
        input('Загадай свой вопрос.\n'
              'Когда будешь готов услышать ответ, нажми клавишу ввода.')
        print(choice(answers), '\n')
        question = input(
            'Ещё вопрос?\n1 - задать вопрос, '
            'любой другой текст - для выхода\n')
        if question == '1':
            print()
        else:
            print('Возвращайся, если возникнут вопросы!')
            break


def main():
    prediction_game()


if __name__ == '__main__':
    main()
