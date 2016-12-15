#!/usr/bin/python3
from random import shuffle, sample
__author__ = 'Ivan Povalyaev'

"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток.
В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""


class Ticket:

    def __init__(self):
        self.ticket = [' ' for x in range(27)]
        random_nums = sorted(sample(range(1, 91), 15), reverse=True)
        random_indexes = sample(range(9), 5)
        random_indexes += sample(range(9, 18), 5)
        random_indexes += sample(range(18, 27), 5)
        for index in sorted(random_indexes):
            self.ticket[index] = random_nums.pop()

    def __str__(self):
        return '{}\n{}\n{}'.format('  '.join(str(x) for x in self.ticket[:9]),
                                   '  '.join(str(x) for x in self.ticket[9:18]),
                                   '  '.join(str(x) for x in self.ticket[18:]))

    def __repr__(self):
        return self.__str__()


class Bag:

    def __init__(self):
        self.index = 90
        self.__bag = [x for x in range(1, 91)]
        shuffle(self.__bag)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.__bag.pop()
        else:
            raise StopIteration

    def __str__(self):
        return '{} бочонков осталось в мешке'.format(self.index)

    def __repr__(self):
        return self.__str__()



class Game:

    def __init__(self, **kwargs):
        self.player1 = kwargs.get('player1', None)
        self.player2 = kwargs.get('player2', None)
        if self.player1 is None or self.player2 is None:
            raise RuntimeError("'player1' or 'player2' wasn't properly setted")
        self.bag = Bag()

    def start(self):
        game_in_progress = True
        for number in self.bag:
            while game_in_progress:
                print('Новый бочонок: {} (осталось {})'.format(
                    number, self.bag.index))
                print('------ Ваша карточка -----')
                print(self.player1.ticket)
                print('--------------------------')
                print('-- Карточка компьютера ---')
                print(self.player2.ticket)
                print('--------------------------')
                answer = input('Зачеркнуть цифру? (y/n): ')
                if answer == 'y':
                    raise Exception


if __name__ == '__main__':
    game = Game()
    game.start()