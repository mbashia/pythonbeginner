def summ(num1, num2):
    summation =num1 + num2
    return summation


def subtract(num1, num2):
    diff = num1 - num2
    return diff


def division(num1, num2):
    division = num1/num2
    return division


def multiplication(num1, num2):
    multi =num1 * num2
    return multi


choice = int(input(""" select operation
1. addition
2.subtraction
3.division
4.multiplication
enter here:
"""))
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
if choice==1:
    print(sum(num1, num2))
elif choice == 2:
    print(subtract(num1, num2))
elif choice == 3:
    print(division(num1, num2))
elif choice == 4:
    print(multiplication(num1, num2))
else:
    print("invalid choice")

