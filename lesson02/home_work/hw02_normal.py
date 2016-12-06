from math import sqrt
from datetime import datetime as dt
import locale
from num2words import num2words
from random import randint
__author__ = 'Povalyaev Ivan'
# Задача-1:
# Дан список, заполненный произвольными целыми числами,
# получите новый список, элементами которого будут
# квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


def create_sqrt_list(list):
    return [int(sqrt(x)) for x in list if x >= 0 and sqrt(x).is_integer()]

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


def get_pretty_date(date):
    dt_object = dt.strptime(date, '%d.%m.%Y')
    locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
    day_in_word = num2words(dt_object.day, lang='ru')
    return dt_object.strftime('{} %B %Y года'.format(day_in_word))

# Задача-3: Напишите алгоритм, заполняющий список произвольными
# целыми числами в диапазоне от -100 до 100
# В списке должно быть n - элементов
# Подсказка: для получения случайного числа изпользуйте функцию randint()
# модуля random


def create_random_list(n):
    return [randint(-100, 100) for x in range(n)]

# Задача-4: Дан список, заполненный произвольными целыми числами
# Получите новый список, элементами которого
# будут только уникальные элементы исходного
# Например, lst = [1,2,4,5,6,2,5,2], нужно получить lst2 = [1,4,6]


def create_unique_list(list):
    return [x for x in list if list.count(x) == 1]


if __name__ == '__main__':
    print(create_sqrt_list([2, -5, 8, 9, -25, 25, 4]))
    print(get_pretty_date('02.11.2013'))
    print(create_random_list(20))
    print(create_unique_list([1, 2, 4, 5, 6, 2, 5, 2]))
