__author__ = 'Povalyaev Ivan'
# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True
# Вопрос: Чему была равна переменная a, если точно известно, что её
# значение не изменялось?


class A(object):

    def __eq__(self, other):
        return True

    def __pow__(self, other):
        return True

    def __mul__(self, other):
        return True

    def __gt__(self, other):
        return True


a = A()
print(a == a ** 2)
print(a == a * 2)
print(a > 999999)
