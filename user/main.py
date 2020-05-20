# a = list(input('please werite something here: '))


class User:
    def __init__(self, name, income, balance):
        self.name = name
        self.income = income
        self.balance = balance

    def create_account(self):
        account = (self.name)
        print(f'account {account} created')

        return account

        # def __str__(self):
    #     return f'{self.name} {self.income} {self.balance}'
    # #
    # def __eq__(self, other):
    #     return (
    #         self.name == other.name,
    #         self.name == other.name,
    #         self.name == other.name,
    #         )


#
a = User('Vasya', 1000, '0')
a.create_account()
# print(a.name, a.balance, a.income)
#
# a = User.name('Vasya')
#
# print(a)
