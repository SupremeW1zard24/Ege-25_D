def f(s, xodi):
    if 45 <= s <= 112: return xodi % 2 == 0  # Условие победы
    if s > 112: return xodi % 2 != 0  # Условие проигрыша
    if xodi == 0: return 0
    nextWin = [f(s + 2, xodi - 1), f(s * 3, xodi - 1)]
    return any(nextWin) if (xodi - 1) % 2 == 0 else all(nextWin)


print([s for s in range(1, 45) if f(s, 2)])  # [41, 42]
print([s for s in range(1, 45) if not f(s, 1) and f(s, 3)])  # [14, 39, 40]
print([s for s in range(1, 45) if not f(s, 2) and f(s, 4)])  # [12, 13, 38]
