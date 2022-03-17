n=8
v1=v2=0
v3=1.5
v_i=0
for i in range(4,n+1):
    v_i=(i+1)/(i**2+1)*v3-v2*v1
    print(v_i)