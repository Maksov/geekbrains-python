#!/usr/bin/python3
"""Упражнение "Количество слов"

Функция main() ниже уже определена и заполнена. Она вызывает функции
print_words() и print_top(), которые вам нужно заполнить.

1. Если при вызове файла задан флаг --count, вызывается функция
print_words(filename), которая подсчитывает, как часто каждое слово встречается
в тексте и выводит:
слово1 количество1
слово2 количество2
...

Выводимый список отсортируйте в алфавитном порядке. Храните все слова
в нижнем регистре, т.о. слова "Слон" и "слон" будут обрабатываться как одно
слово.

2. Если задан флаг --topcount, вызывается функция print_top(filename),
которая аналогична функции print_words(), но выводит только топ-20 наиболее
часто встречающихся слов, таким образом первым будет самое часто встречающееся
слово, за ним следующее по частоте и т.д.

Используйте str.split() (без аргументов), чтобы разбить текст на слова.

Отсекайте знаки припинания при помощи str.strip() с знаками припинания
в качестве аргумента.

Совет: не пишите всю программу сразу. Доведите ее до какого-то промежуточного
состояния и выведите вашу текущую структуру данных. Когда все будет работать
как надо, перейдите к следующему этапу.

Дополнительно: определите вспомогательную функцию, чтобы избежать дублирования
кода внутри print_words() и print_top().

"""

import os
import re
import sys
from collections import Counter
__author__ = 'Поваляев Иван'

# +++ваш код+++
# Определите и заполните функции print_words(filename) и print_top(filename).
# Вы также можете написать вспомогательную функцию, которая читает файл,
# строит по нему словарь слово/количество и возвращает этот словарь.
# Затем print_words() и print_top() смогут просто вызывать эту
# вспомогательную функцию.


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def text_prettifyer(text):
    return text.lower().replace('\n', ' ').replace('\r', ' ')


def get_all_words(text, top=20):
    all_words = re.findall('\w+', text)
    all_words_dict = Counter(all_words)
    if top is None:
        return sorted(all_words_dict.items(), key=lambda x: x[0])
    return all_words_dict.most_common(top)


def print_words(all_words):
    for word in all_words:
        _word = word[0]
        _word_count = word[1]
        print('Слово "{}" - кол-во в тексте {}'.format(_word, _word_count))

###

# Это базовый код для разбора аргументов коммандной строки.
# Он вызывает print_words() и print_top(), которые необходимо определить.


def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    data = load_data(filename)
    pretty_text = text_prettifyer(data)
    if option == '--count':
        words = get_all_words(pretty_text, top=None)
        print_words(words)
    elif option == '--topcount':
        most_frequent_words = get_all_words(pretty_text)
        print_words(most_frequent_words)
    else:
        print('unknown option: ' + option)
    sys.exit(1)


if __name__ == '__main__':
    main()
