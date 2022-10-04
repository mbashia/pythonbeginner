def triangle_area(h, b):
    area = 0.5 * h * b
    return area
h = int(input("enter the height of the triangle:"))
b = int(input("enter the base of the triangle:"))
print(triangle_area(h, b))