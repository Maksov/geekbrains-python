__author__ = 'Поваляев Иван'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим
# правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math


def my_round(number, ndigits):
    # cutted_number = str(number)[:ndigits + 2]
    # if int(cutted_number[-1]) < 5:
    #     return float(cutted_number[:ndigits + 1])
    # return float(cutted_number[:ndigits] + str(int(cutted_number[-2]) + 1))
    return '{0:.{1}f}'.format(number, ndigits)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


class Ticket():

    def __init__(self, ticket_number):
        self.ticket_number = ticket_number
        self.lucky = self.is_lucky()

    def __str__(self):
        if self.lucky:
            return ("Поздравляем! Ваш билет"
                    " {} счастливый".format(self.ticket_number))
        else:
            return ("Извините! Ваш билет"
                    " {} не счастливый".format(self.ticket_number))

    def is_lucky(self):
        first_part_sum = sum((int(x) for x in str(self.ticket_number)[:3]))
        last_part_num = sum((int(x) for x in str(self.ticket_number)[3:]))
        return True if first_part_sum == last_part_num else False


if __name__ == '__main__':
    ''' Задача 1 '''
    print(my_round(2.1234567, 5))
    print(my_round(2.1234467, 5))
    print()
    ''' Задача 2 '''
    lucky_ticket = Ticket(343730)
    print(lucky_ticket)
    not_lucky_ticket = Ticket(333730)
    print(not_lucky_ticket)
