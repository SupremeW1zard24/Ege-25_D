def f(a, b, m):
    if a + b >= 83: return m % 2 == 0
    if m == 0: return 0
    nextWin = [f(a + 1, b, m - 1), f(a * 4, b, m - 1), f(a, b + 1, m - 1), f(a, b * 4, m - 1)]
    return any(nextWin) if (m - 1) % 2 == 0 else all(nextWin)  # Для 19 поменять all на any


print([s for s in range(1, 78) if f(5, s, 2)])  # 3
print([s for s in range(1, 78) if not f(5, s, 1) and f(5, s, 3)])  # 2 19
print([s for s in range(1, 78) if not f(5, s, 2) and f(5, s, 4)])  # 18
