x, y, z = input("enter three  numbers:").split()
x = int(x)
y = int(y)
z = int(z)
number = [x, y, z]
for item in number:
    maxim = x
    if item > maxim:
        maxim = item
print(maxim)

