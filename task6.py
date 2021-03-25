"""
Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое,
и False - иначе.
"""
""""
Простое число всегда является положительным целым числом и делится ровно на 2 целых числа (1 и само число),
 1 не является простым числом.
"""


def IsPrime2(n):
    if n < 2:
        return False
    d = 2
    while n % d != 0:
        d += 1
    return d == n

