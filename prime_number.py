# program to check if number entered is prime
num = int(input("enter number to be checked:"))
is_prime = False
for i in range(2, num):
    if (num % i) == 0:
        is_prime = True
        print(num, "is not prime")
        break
    else:
        is_prime = False

        print(num, "is prime")
        break