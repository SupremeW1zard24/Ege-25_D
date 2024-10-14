def game(a, b, xod):
    if a + b >= 75: return xod % 2 == 0
    if xod == 0: return 0
    nextWin = [game(a + 1, b, xod - 1), game(a * 2, b, xod - 1), 
               game(a, b + 1, xod - 1), game(a, b * 2, xod - 1)]
    return any(nextWin) if (xod - 1) % 2 == 0 else all(nextWin)


print([s for s in range(1, 67) if game(8, s, 2)])  # [17]
print([s for s in range(1, 67) if not game(8, s, 1) and game(8, s, 3)])  # [29, 32]
print([s for s in range(1, 67) if game(8, s, 4) and not game(8, s, 2)])  # [28]
