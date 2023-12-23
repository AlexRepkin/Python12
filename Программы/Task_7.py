#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


def recursion_factorial(n):
    """Рекурсивное вычисление факториала."""

    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n - 1)


def recursion_fib(n):
    """Рекурсивное вычисление числа Фибоначчи."""

    if 1 >= n >= 0:
        return n
    else:
        return recursion_fib(n - 2) + recursion_fib(n - 1)


def iterative_factorial(n):
    """Итеративное вычисление факториала."""

    value = 1
    while n > 1:
        value *= n
        n -= 1
    return value


def iterative_fib(n):
    """Итеративное вычисление числа Фибоначчи."""

    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


@lru_cache
def recursion_factorial_lru(n):
    """
    Рекурсивное вычисление факториала
    с использование декоратора lru_cache.
    """

    if n == 0:
        return 1
    else:
        return n * recursion_factorial_lru(n - 1)


@lru_cache
def recursion_fib_lru(n):
    """
    Рекурсивное вычисление числа Фибоначчи
    с использование декоратора lru_cache.
    """

    if 1 >= n >= 0:
        return n
    else:
        return recursion_fib_lru(n - 2) + recursion_fib_lru(n - 1)


if __name__ == '__main__':
    """
    Замер времени, ушедшего на вычисление функциями.
    В список spent_time складируются полученные результаты.
    timeit позволяет проанализировать потраченное время, если
    передать ему функцию и количество повторений (По умолчанию 1000000).
    Функция передаётся в кавычках, чтобы у timeit был доступ к её вызову,
    пришлось также указывать globals=globals(), так, функция стала глобальной.
    """

    spent_time = list()
    repeats = 50
    for i in range(10, 26):
        needed_value = str(i)

        # Время работы recursion_factorial
        time_recursion_factorial = timeit.timeit(
            "recursion_factorial("+needed_value+")", globals=globals(), number=repeats)
        spent_time.append(("Recursion Factorial", i, time_recursion_factorial))

        # Время работы iterative_factorial
        time_iterative_factorial = timeit.timeit(
            "iterative_factorial("+needed_value+")", globals=globals(), number=repeats)
        spent_time.append(("Iterative Factorial", i, time_iterative_factorial))

        # Время работы recursion_factorial_lru
        time_recursion_factorial_lru = timeit.timeit(
            "recursion_factorial_lru("+needed_value+")", globals=globals(), number=repeats)
        spent_time.append(("Recursion Factorial with lru_cache",
                          i, time_recursion_factorial_lru))

        # Время работы recursion_fib
        time_recursion_fib = timeit.timeit(
            "recursion_fib("+needed_value+")", globals=globals(), number=repeats)
        spent_time.append(("Recursion Fib", i, time_recursion_fib))

        # Время работы iterative_fib
        time_iterative_fib = timeit.timeit(
            "iterative_fib("+needed_value+")", globals=globals(), number=repeats)
        spent_time.append(("Iterative Fib", i, time_iterative_fib))

        # Время работы recursion_fib_lru
        time_recursion_fib_lru = timeit.timeit(
            "recursion_fib_lru("+needed_value+")", globals=globals(), number=repeats)
        spent_time.append(("Recursion Fib with lru_cache",
                          i, time_recursion_fib_lru))

    # Вывод результатов
    for name, i, time_spent in spent_time:
        print(f"{name} {i}: {time_spent:.6f}")
