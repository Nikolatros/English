from cards import Cards


while True:
    try: 
        topic = input('Название темы(air pollution):\n')
        cards = {}
        with open(f'{topic}.txt', encoding='utf-8') as study_file:
            for row in study_file:
                en_word, translation = row.split('; ')
                cards[en_word] = list(translation[:-1].split('\\ '))
        print('Запуск..\n')
        break
    except OSError:
        print('Ошибка. Такого файла нет.')

a = Cards(cards)
a.ru_en()
