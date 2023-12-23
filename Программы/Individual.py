#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def create_brackets(combination, open_amount, close_amount, variants):
    """
    Данная рекурсивная функция генерирует все комбинации закрывающихся
    и открывающихся скобок. На вход она получает текущую комбинацию
    (это combination), оставшееся количество неиспользованных скобок 
    (Открывающиеся - open_amount, Закрывающиеся - close_amount) и
    все полученные варианты (variants).
    """

    # Если не осталось доступных для исп. открывающихся и закрывающихся
    # скобок, то добавляем полученную комбинацию.
    if open_amount == 0 and close_amount == 0:
        variants.append(combination)
    # Если ещё есть открывающиеся, то добавляем их и запускаем с уменьшенным кол.
    if open_amount > 0:
        create_brackets(
            combination + "(", open_amount - 1, close_amount, variants)
    # Если ещё есть закрывающиеся и их меньше, чем открывающихся,
    # то добавляем их и запускаем с уменьшенным кол.
    if close_amount > 0 and open_amount < close_amount:
        create_brackets(combination + ")", open_amount,
                        close_amount - 1, variants)
    return variants


if __name__ == '__main__':
    """Получение количества пар от пользователя и вызов функции."""

    n = int(input("Good day! Please, enter amount of pairs - "))
    result = []
    result = create_brackets("", n, n, result)
    print("All possible variants are:", " ; ".join(result))
