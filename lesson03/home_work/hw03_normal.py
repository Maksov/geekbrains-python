__author__ = 'Povalyaev Ivan'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fibo_list = [1, 1]
    for number in range(m - 2):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    fibo_elements = [x for x in fibo_list[n - 1:m]]
    return 'Элементы ряда Фибоначчи с {} по {}: {}'.format(n, m, fibo_elements)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать
# встроенную функцию и метод sort()


def sort_to_max(origin_list):
    new_list = []
    while len(origin_list) != 0:
        minimal_value = min(origin_list)
        origin_list.remove(minimal_value)
        new_list.append(minimal_value)
    return 'Отсортированный список: {}'.format(new_list)


# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter(func, iterable):
    return [x for x in iterable if func(x)]


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def rhomboid(dots):
    a, b, c, d = dots
    half_ac = ((a[0] + c[0]) / 2, (a[1] + c[1]) / 2)
    half_db = ((d[0] + b[0]) / 2, (d[1] + b[1]) / 2)
    if half_ac == half_db:
        return True
    else:
        return False


if __name__ == '__main__':
    ''' Задача 1 '''
    print(fibonacci(5, 10))
    ''' Задача 2 '''
    print()
    print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
    ''' Задача 3 '''
    print()
    print('Первоначальный список: {}'.format([-1, -2, -3, 0, 1, 2, 3, 4]))
    print('Функция lambda x: x > 0')
    print('Отсортированный список: ', end='')
    print(filter(lambda x: x > 0, [-1, -2, -3, 0, 1, 2, 3, 4]))
    ''' Задача 4 '''
    print()
    dots = ((0, 0), (4, 0), (4, 4), (0, 4))
    if rhomboid(dots):
        print('Точки A1{} A2{} A3{} A4{} являются '
              'вершинами параллелограмма'.format(*dots))
    else:
        print('Точки A1{} A2{} A3{} A4{} '
              'не являются вершинами параллелограмма'.format(*dots))
