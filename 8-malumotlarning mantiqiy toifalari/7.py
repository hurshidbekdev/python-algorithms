n=50
for a in range(1,n+1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            if c**2==b**2+a**2:
                print(f'a={a},b={b},c={c}')