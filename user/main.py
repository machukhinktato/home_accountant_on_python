# a = list(input('please werite something here: '))


class User:
    def __init__(self, name, income, balance):
        self.name = name
        self.income = income,
        self.balance = balance

    def __str__(self):
        return self.__all__()

    def __eq__(self, other):
        return (
            self.name == other.name,
            self.name == other.name,
            self.name == other.name,
            )
