#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def knapsack_with_reps_bu(W, weights, costs):
    n = len(weights)
    D = [0] * (W + 1)

    for w in range(1, W + 1):
        for i in range(n):
            if weights[i] <= w:
                D[w] = max(D[w], D[w - weights[i]] + costs[i])

    return D[W]


def knapsack_without_reps_bu(W, weights, costs):
    n = len(weights)
    D = [[0 for _ in range(n + 1)] for _ in range(W + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            D[w][i] = D[w][i - 1]
            if weights[i - 1] <= w:
                D[w][i] = max(D[w][i], D[w - weights[i - 1]]
                              [i - 1] + costs[i - 1])

    return D[W][n]


def knapsack_td(w, n, weights, values, H):
    if w not in H:
        v = 0
        for i in range(1, n+1):
            if weights[i-1] <= w:
                v = max(v, knapsack_td(
                    w - weights[i-1], n, weights, values, H) + values[i-1])
        H[w] = v
    return H[w]


if __name__ == "__main__":
    # Для задачи о рюкзаке с повторениями
    W = 50  # Вместимость рюкзака
    weights = [10, 20, 30]  # Веса предметов
    costs = [60, 100, 120]  # Стоимости предметов
    print("Решение задачи о рюкзаке с повторениями с использованием "
          "динамического программирования снизу вверх:",
          knapsack_with_reps_bu(W, weights, costs))

    # Для задачи о рюкзаке без повторений
    print("Решение задачи о рюкзаке без повторений с использованием "
          "динамического программирования снизу вверх:",
          knapsack_without_reps_bu(W, weights, costs))

    n = len(costs)
    H = {}

    max_value = knapsack_td(W, n, weights, costs, H)
    print("Решение задачи о рюкзаке сверху вниз: ", max_value)