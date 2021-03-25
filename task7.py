"""Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем
календаре, и False иначе. """
from datetime import date as dat


def date(dd, mm, yyyy):
    try:
        dat(year=yyyy, month=mm, day=dd)
        return True
    except ValueError:
        return False


print(date(29, 2, 2020))
