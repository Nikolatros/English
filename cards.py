import random


class Cards():

    def __init__(self, cards: dict):
        self.cards_top = list(cards.items())
        self.cards_middle = []
        self.cards_bot = []
        self.cards_list = [self.cards_top, self.cards_middle, self.cards_bot] 
        self.last_word = None


    def ru_en(self):
        

        def dict_index_choice():
            """
            Выбирает 'стопку' карт с указанной вероятностью.


            Returns:
                _int_ : Индекс выбронной 'стопки'
            """            
            while 1:  
                selected_index = random.choices([0, 1, 2], [6, 3, 1])[0]
                if len(self.cards_list[selected_index]) != 0:
                    return selected_index 


        while 1:
            index = dict_index_choice()
            cards = self.cards_list[index]
            pair = cards.pop(cards.index(random.choice(cards)))
            # выбираем случайную пару из 'стопки'
            en_word, translate_words = pair
            if en_word == self.last_word:
                # если новое слово совпадает с предыдущим, то возвращаем его на место
                cards.append(pair)
                continue
            
            print(','.join(translate_words))
            
            input_word = input('::: ')
            mistake = en_word != input_word

            if mistake == False:
                # если ошибки нет, то перемещаем пару на одну колоду выше (если пара не из верхней стопки)
                self.cards_list[min(index + 1, 2)].append(pair)
            else:
                while mistake:
                    # пока пользователь вводит неправильное слово
                    print(en_word) 
                    input_word = input('::: ')
                    mistake = en_word != input_word                 
                else:
                    # в конце перемещаем пару на одну колоду ниже (если пара не из нижней стопки)
                    self.cards_list[max(index - 1, 0)].append(pair)
            print('# Correct!', end=' ')
            print([len(i) for i in self.cards_list], '\n')
            self.last_word = en_word # 'сохраняем' последнее выданное слово
