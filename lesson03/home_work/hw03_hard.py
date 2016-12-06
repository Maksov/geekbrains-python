import os
import re
from copy import deepcopy
__author__ = 'Поваляев Иван'
# Задание-1:
# Написать программу, выполняющую операции
# (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть,
# x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части,
# или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 2/3


def get_fractions_with_operand(expression):
    ''' Функция возвращает приведенные дроби и оператор выражения '''
    operands = []
    # Получаем оператор выражения
    operator = re.search('.[-+].', expression).group(0).strip()
    # Получаем сырые операнды
    parts = re.split('.[-+].', expression)
    for operand in parts:
        # Разделяем операнд
        operand_parts = operand.split()
        # Если длина списка равна 2-м, то есть целая и дробная части
        if len(operand_parts) == 2:
            # Преобразуем целую часть операнда для последующих вычислений
            first_operand_part = int(operand_parts[0])
            last_operand_part = operand_parts[1]
            # Разделяем дробную часть для последующих вычислений
            fraction_parts = last_operand_part.split('/')
            # Перемножаем знаменатель из дробной части и целую часть
            numerator_part = int(fraction_parts[1]) * first_operand_part
            if numerator_part < 0:
                # Если выражение отрицательное, вычитаем числитель
                numerator = numerator_part - int(fraction_parts[0])
            else:
                # Если положительное, прибавляем числитель
                numerator = numerator_part + int(fraction_parts[0])
            # Для читаемости указываем переменную для знаменателя
            denominator = fraction_parts[1]
            operands.append('{}/{}'.format(numerator, denominator))
        # в противном случае имеем только дробную часть
        else:
            operands.append(operand)
    return operands, operator


def sum_fractions(operands, operator):
    ''' Функция возвращает результат операции с двумя дробями'''
    # Первый числитель
    first_numerator = int(operands[0].split('/')[0])
    # Первый знаменатель
    first_denominator = int(operands[0].split('/')[1])
    # Второй числитель
    second_numerator = int(operands[1].split('/')[0])
    # Второй знаменатель
    second_denominator = int(operands[1].split('/')[1])
    # Получаем итоговый знаменатель
    common_denominator = first_denominator * second_denominator
    if operator == '+':
        common_numerator = first_numerator * second_denominator + \
            second_numerator * first_denominator
    else:
        common_numerator = first_numerator * second_denominator - \
            second_numerator * first_denominator
    # Проверяем что числитель больше знаменателя
    if abs(common_numerator) >= common_denominator:
        floor_part = int(common_numerator / common_denominator)
        fraction_numerator = abs(common_numerator) % common_denominator
        fraction_denominator = common_denominator
        return '{} {}/{}'.format(floor_part,
                                 fraction_numerator, fraction_denominator)
    return '{}/{}'.format(common_numerator, common_denominator)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def load_data(filepath, exclude_header=False):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        if exclude_header:
            next(file_handler)
        return file_handler.readlines()


def create_employees_dict(employees_data):
    names = (' '.join(x.split()[:2]) for x in employees_data)
    wages = (int(x.split()[2]) for x in employees_data)
    planed_hours = (int(x.strip('\n').split()[4]) for x in employees_data)
    return dict(zip(names, [list(x) for x in zip(wages, planed_hours)]))


def create_employees_hours_dict(hours_data):
    names = (' '.join(x.split()[:2]) for x in hours_data)
    worked_hours = (int(x.strip('\n').split()[-1]) for x in hours_data)
    return dict(zip(names, worked_hours))


def create_full_dict(employees, worked_hours):
    employees_copy = deepcopy(employees)
    for name in employees_copy:
        employees_copy[name].append(worked_hours[name])
    return employees_copy


def calculate_wage(full_employees_data):
    full_employees_data_copy = deepcopy(full_employees_data)
    for name, data in full_employees_data_copy.items():
        wage = data[0]
        planed_hours = data[1]
        worked_hours = data[2]
        if planed_hours >= worked_hours:
            real_wage = wage * worked_hours / planed_hours
        else:
            overtime = worked_hours - planed_hours
            overtime_wage = overtime * wage / planed_hours
            real_wage = wage * planed_hours / planed_hours + overtime_wage
        data.append(real_wage)
    return full_employees_data_copy


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв,
# имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


def get_fruits_dict(fruits):
    fruits_dict = {}
    fruits_capitals = (first_letter[0] for first_letter in fruits)
    for letter in fruits_capitals:
        fruits_dict[letter] = [x for x in fruits if letter == x[0]]
    return fruits_dict


def write_fruits_to_files(fruits_dict):
    for letter, fruits in fruits_dict.items():
        filename = os.path.join('data', 'fruits_{}'.format(letter))
        with open(filename, 'w+') as f_handler:
            f_handler.write('\n'.join(fruits))


if __name__ == '__main__':
    ''' Задача 1 '''
    operands, operator = get_fractions_with_operand('-1/2 - 2 1/3')
    print(sum_fractions(operands, operator))
    operands, operator = get_fractions_with_operand('1 1/5 + -3 3/4')
    print(sum_fractions(operands, operator))
    operands, operator = get_fractions_with_operand('-1 1/12 + 12/17')
    print(sum_fractions(operands, operator))
    operands, operator = get_fractions_with_operand('-1 1/12 + -12/17')
    print(sum_fractions(operands, operator))
    ''' Задача 2 '''
    print()
    filename = os.path.join('data', 'workers')
    employees_data = load_data(filename, exclude_header=True)
    employees = create_employees_dict(employees_data)
    filename = os.path.join('data', 'hours_of')
    worked_hours_data = load_data(filename, exclude_header=True)
    worked_hours = create_employees_hours_dict(worked_hours_data)
    full_employees_data = create_full_dict(employees, worked_hours)
    full_employees_data_with_wages = calculate_wage(full_employees_data)
    print('{:<20}{}'.format('Сотрудник', 'Зарплата'))
    for name, data in full_employees_data_with_wages.items():
        print('{:<20}{:.2f}'. format(name, data[3]))
    ''' Задача 3 '''
    print()
    filename = os.path.join('data', 'fruits.txt')
    fruits = [x.strip('\n') for x in load_data(filename) if x != '\n']
    fruits_dict = get_fruits_dict(fruits)
    write_fruits_to_files(fruits_dict)
