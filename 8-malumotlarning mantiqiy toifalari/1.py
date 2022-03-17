a=True
b=False
c=True
d=False
print((a and b) or (c and d)) and (a or b)


# -----1------
a=True
b=False
c=True
d=False
print((a and b) or (c and d)) or (a or b)

# ------2----

a=True
b=False
c=True
d=False
print((a and b) or (c and d)) and (a or b)

# ---3----

a=True
b=False
c=True
d=False
c=((a and b) or (c and d))
