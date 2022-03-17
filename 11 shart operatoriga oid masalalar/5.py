x=1
y=-2
z=-3
if x>y>0>z:
    print(f'mus={2},min={1}')
elif x>0>y>z:
    print(f'mus={1},min={2}')
elif y>x>0:
    print(f'mus={2},min={1}')
elif y>0>x>z:
    print(f'mus={1},min={2}')
elif z>x>0>y:
    print(f'mus={2},min={1}')
elif z>0>x>y:
    print(f'mus={1},min={2}')