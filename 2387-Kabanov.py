def f(a, b, m):
    if a + b >= 45: return m % 2 == 0
    if m == 0: return 0
    nextWin = [f(a + 1, b, m - 1), f(a * 3, b, m - 1), f(a, b + 1, m - 1), f(a, b * 3, m - 1)]
    return any(nextWin) if (m - 1) % 2 == 0 else all(nextWin)


print([s for s in range(1, 41) if f(4, s, 2)])  # all нужно разово сменить на any для этого пункта (неудачный ход) -> any(nextWin)
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
# 34, 35, 36, 37, 38, 39] ---> Выбираем 5 (меньшее по условию)
print([s for s in range(1, 41) if not f(4, s, 1) and f(4, s, 3)])  # [8, 13]
print([s for s in range(1, 41) if not f(4, s, 2) and f(4, s, 4)])  # [12]
