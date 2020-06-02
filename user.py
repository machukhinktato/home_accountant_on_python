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
    income = []
    balance = []
    wish_to_save = []


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
Builder = director.construct

if __name__ == '__main__':
    Builder(user__builder, 'Василий', 1000, 1500, 500)
    user = user__builder.person
    print(user.__dict__)
    user.income.append(200)
    print(user.__dict__)