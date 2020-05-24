import abc


class UserBuildDirector:
    def __init__(self):
        self._builder = None

    def construct(self, builder, name, income, balance, wish_to_save):
        self._builder = builder
        self._builder._build_name(name)
        self._builder._build_income(income)
        self._builder._build_balance(balance)
        self._builder._build_wish_to_save(wish_to_save)


class User:
    name = ''
    income = 0
    balance = 0
    wish_to_save = 0


class AbstractTableBuilder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.person = User()

    @abc.abstractmethod
    def _build_name(self):
        pass

    @abc.abstractmethod
    def _build_income(self):
        pass

    @abc.abstractmethod
    def _build_balance(self):
        pass

    @abc.abstractmethod
    def _build_wish_to_save(self):
        pass


class UserBuilder(AbstractTableBuilder):
    def _build_name(self, name):
        self.person.name = name

    def _build_income(self, income):
        self.person.income = income

    def _build_balance(self, balance):
        self.person.balance = balance

    def _build_wish_to_save(self, wish_to_save):
        self.person.wish_to_save = wish_to_save


user__builder = UserBuilder()
director = UserBuildDirector()

if __name__ == '__main__':
    director.construct(user__builder, 'Василий', 1000, 1500, 500)
    Vasya = user__builder.person
    print(f'Пользователь {Vasya.name}, с доходом {Vasya.income} рублей, '
          f'и балансом в настоящий момент {Vasya.balance} рублей,\n'
          f'Хочет по окончанию отчетного периода иметь не менее '
          f'{Vasya.wish_to_save} рублей')
