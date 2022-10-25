class Employee:
    def __init__(self, firstname, second_name):
        self.firstname = firstname
        self.secondname = second_name

    def get_fullname(self):
        return f"{self.firstname}   {self.secondname}"


class SoftwareEngeenier(Employee):
    def __init__(self, firstname, secondname, age, level):
        super().__init__(firstname, secondname)
        self.level = level
        self.age = age


class Designer(Employee):
    pass


se = SoftwareEngeenier('victor', 'mbashia', '20', 'senior')
print(se.firstname)


# e1 = Employee()
e1 = Employee("victor", "mbashia")


