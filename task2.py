"""
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
"""
'''
В високосном годе 366 дней, в обычном 365.

1 Если год не делится на 4, значит он обычный.
2 Иначе надо проверить не делится ли год на 100.
3 Если не делится, значит это не столетие и можно сделать вывод, что год високосный.
4 Если делится на 100, значит это столетие и его следует проверить его делимость на 400.
5 Если год делится на 400, то он високосный.
6 Иначе год обычный.
'''


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True