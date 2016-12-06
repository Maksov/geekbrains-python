from random import randint
__author__ = 'Поваляев Иван'

# Задача-1: Дано произвольное целое число, вывести поочередно цифры
# исходного числа
print('*' * 40)
number = str(randint(1, 100))
print('Исходное число: {}'.format(number))
for num, place in enumerate(number, start=1):
    print('{}-ая цифра: {}'.format(num, place))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так: print("a = ", b, "b = ", a) - это
# неправильное решение!
print('*' * 40)
a = input('Введите значение переменной a: ')
b = input('Введите значение переменной b: ')
print('Текущее значение переменной a = {}'.format(a))
print('Текущее значение переменной b = {}'.format(b))
print('Производим обмен значениями')
a, b = b, a
print('Текущее значение переменной a = {}'.format(a))
print('Текущее значение переменной b = {}'.format(b))


# Задача-3: Запросите у пользователя его возраст. Если ему есть 18 лет,
# выведите: "Доступ разрешен", иначе "Извините, пользование данным ресурсом
# только с 18 лет"
print('*' * 40)
age = int(input('Пожалуйста введите Ваш возраст: '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')
