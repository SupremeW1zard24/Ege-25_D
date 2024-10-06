def f(s, xodi):
    if s >= 25: return xodi % 2 == 0
    if xodi == 0: return 0
    nextWin = [f(s + 2, xodi - 1), f(s * 2, xodi - 1)]
    return any(nextWin) if (xodi - 1) % 2 == 0 else all(nextWin)


print([s for s in range(1, 25) if f(s, 2)])   #[11, 12]
print([s for s in range(1, 25) if not f(s, 1) and f(s, 3)])   #[6, 9, 10]
print([s for s in range(1, 25) if f(s, 4) and not f(s, 2)])   #[7, 8]
