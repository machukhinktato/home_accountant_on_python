# a = list(input('please werite something here: '))


class User:
    def __init__(self, name, income, balance):
        self.name = name
        self.income = income
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.income} {self.balance}'
    #
    # def __eq__(self, other):
    #     return (
    #         self.name == other.name,
    #         self.name == other.name,
    #         self.name == other.name,
    #         )

#
# a = User('Vasya', 1000, '0')
# print(a.name, a.balance, a.income)

a = User('Vasya', 1000, '0')

print(a)