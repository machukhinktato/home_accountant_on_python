class User:
    def __init__(self, name):
        self.name = name
        self.category = set()
        self.account = {}
        self.balance = []

    def __str__(self):
        return f'{self.name}'



if __name__ == '__main__':
    user = User('Misha')
    bank = Bank()
    bank.expense_account.append(500)
    print(bank.expense_account[0])
    products = Category('products')
    print(products)
