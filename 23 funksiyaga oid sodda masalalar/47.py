def ekub(a,b):
    while a>b:
        if a!=b:
            a-=b
        else:
            b-=a
            print(a)
ekub(34,6)