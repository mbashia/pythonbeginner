class SoftwareEngineer:
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    skill = ''

    def coding(self, se):
        print(f'{se.name} is coding ...')


se1 = SoftwareEngineer('Mbashia', 20, 'junior', 6000)
se1.skill = "keyboard warrior"
print(se1.skill)
print(se1.name)
print(se1.salary)
