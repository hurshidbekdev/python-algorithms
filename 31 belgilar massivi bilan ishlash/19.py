num='123.4'
if num.isnumeric():
    print(1)
elif num.find('.'):
    print(2)
else:
    print(0)