def time(t):
    h=0
    m=0
    s=0
    h=t//3600
    t%=3600
    m=t//60
    t%=60
    s=t
    print(f'h={h},m={m},s={s}')
time(400)