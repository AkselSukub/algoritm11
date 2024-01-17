#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def lis_bottom_up(A):
    n = len(A)
    D = [1] * n
    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    ans = max(D)
    return ans


def lis_bottom_up_2(A):
    n = len(A)
    D = [1] * n
    prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                prev[i] = j
    ans = max(D)
    return ans, prev, D


def restore_answer(D, prev, ans):
    L = [0] * ans
    k = 1
    n = len(D)
    for i in range(2, n):
        if D[i] > D[k]:
            k = i
    j = ans
    while k > 0:
        L[j-1] = k
        j -= 1
        k = prev[k]
    return L


if __name__ == "__main__":
    # Для вычисления наибольшей возрастающей подпоследовательности
    A = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print("Вычисление наибольшей возрастающей подпоследовательности"
          " с использованием динамического программирования снизу вверх:",
          lis_bottom_up(A))
    ans, prev, D = lis_bottom_up_2(A)
    print("Вычисление наибольшей возрастающей подпоследовательности с "
          "использованием динамического программирования снизу вверх (2):",
          ans, "\nВосстановленный ответ:",
          restore_answer(D, prev, ans))