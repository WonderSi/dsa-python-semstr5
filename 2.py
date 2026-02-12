a = [1, 2]
print(a)
print(id(a))

a[1] = 3
print(a)
print(id(a))

b = a
print(id(b))
b[0] = 100

print(a)
