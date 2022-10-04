num = int(input("enter number to be computed:"))
factorial = 1
if num < 0:
    print("factorial is not defined for negative numbers")

elif num == 0:
    print(" the factorial for 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print(factorial)


