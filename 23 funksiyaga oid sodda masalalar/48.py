def ekub(a,b):
    s=a-b
    ekuk=0
    while s>b:
        s-=b
        ekuk=a*b/s
    print(ekuk)
ekub(34,6)