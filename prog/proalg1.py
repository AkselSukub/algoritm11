#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_td(n, F):
    if F[n] == -1:
        if n <= 1:
            F[n] = n
        else:
            F[n] = fib_td(n - 1, F) + fib_td(n - 2, F)
    return F[n]


def fib_bu(n):
    F = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


def fib_bu_improved(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(n - 1):
        next_val = prev + curr
        prev, curr = curr, next_val
    return curr


if __name__ == "__main__":
    # Для вычисления числа фиббоначи
    n = 10
    F = [-1] * (n + 1)
    print("Вычисление числа Фибоначчи рекурсивное:", fib_recursive(n))
    print("Вычисление числа Фибоначчи с использованием"
          " динамического программирования сверху вниз:", fib_td(n, F))
    print("Вычисление числа Фибоначчи с использованием"
          " динамического программирования снизу вверх:", fib_bu(n))
    print("Вычисление числа Фибоначчи с использованием улучшенной версии"
          " динамического программирования снизу вверх:", fib_bu_improved(n))