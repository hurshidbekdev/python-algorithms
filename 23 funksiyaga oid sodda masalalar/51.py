def isLeapyear(n):
 if n%400==0:
    print('true')
 elif n%4==0:
    if n%100!=0:
        print('true')
    else:
        print('false')
 else:
    print('false')
isLeapyear(2000)