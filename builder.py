import abc


class HomeBudgetBuildDirector:
    def __init__(self):
        self._builder = None

    def construct(self, builder, name, income, balance, wish_to_save, category,
                  expense, total_gain):
        self._builder = builder
        self._builder._build_name(name)
        self._builder._build_income(income)
        self._builder._build_balance(balance)
        self._builder._build_wish_to_save(wish_to_save)
        self._builder._build_category(category)
        self._builder._build_expense(expense)
        self._builder._build_total_gain(total_gain)


class HomeBudget:
    name = ''
    income = []
    balance = []
    wish_to_save = []
    category = {}
    expense = []
    total_gain = 0


class AbstractTableBuilder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.person = HomeBudget()

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
    def _build_category(self):
        pass

    @abc.abstractmethod
    def _build_expense(self):
        pass

    @abc.abstractmethod
    def _build_total_gain(self):
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

    def _build_category(self, category):
        self.person.category = category

    def _build_expense(self, expense):
        self.person.expense = expense

    def _build_total_gain(self, total_gain):
        self.person.total_gain = total_gain


user__builder = UserBuilder()
director = HomeBudgetBuildDirector()

if __name__ == '__main__':
    director.construct(user__builder, 'Василий', 1000, 1500, 500, 'trata', 1000, 0)
    Vasya = user__builder.person
    print(f'Пользователь {Vasya.name}, с доходом {Vasya.income} рублей, '
          f'и балансом в настоящий момент {Vasya.balance} рублей,\n'
          f'Хочет по окончанию отчетного периода иметь не менее '
          f'{Vasya.wish_to_save} рублей'
          f'{Vasya.category}, {Vasya.expense}, {Vasya.total_gain}')
