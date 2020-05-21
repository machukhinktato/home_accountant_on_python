# a = list(input('please werite something here: '))


class User:
    def __init__(self, name, income, balance, target):
        self.name = name
        self.income = income
        self.balance = balance
        self.target = target

    def __str__(self):
        return f'Имя клиента {self.name}, ''\n' \
               f'Доход {self.income} руб, ' '\n' \
               f'На счете {self.balance} руб, ' '\n' \
               f'Желаемый остаток на конец месяца {self.target} руб'

    def create_user(self, name, income, balance, target):
        account = {
            'name': name,
            'income': income,
            'balance': balance,
            'target': target
        }

        return {'account': account}

    def edit_user(self, account):
        self.account = account

        return account



if __name__ == '__main__':
    a = User('Vasya', 50000, 10000, 5000)
    b = User.create_user('Misha', 50000, 10000, 5000, 5)
    print(a, '\n',  b)
