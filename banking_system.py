import os


class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_user_details(self):
        symbol = '============================================'
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        return symbol


class Account(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("insufficient funds | Your balance is $", self.balance)
        else:
            self.balance -= withdraw_amount
            print("you balance is $", self.balance)

    def view_balance(self):
        print(self.display_user_details())
        print("you balance is $", self.balance)
        return self.balance


customer = User('mbashia', 20, 'male')
customer = Account('mbashia', 20, 'male')
print("welcome to the bank")


while True:
    print("""1.view balance
2.deposit
3.withdraw
4.exit""")
    print("")

    choice = input("ENTER...")
    if choice == '1':
        print(customer.view_balance())
    elif choice == '2':
        amount = int(input("enter amount you wish to deposit:"))
        customer.deposit(amount)
    elif choice == '3':
        withdraw_amount = int(input("enter amount you wish to withdraw:"))
        customer.withdraw(withdraw_amount)
    elif choice == '4':
        print("Thank you for banking with us")
        break

