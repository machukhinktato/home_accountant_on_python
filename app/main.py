import sys


class MainAccountant:
    def __init__(self, session):
        self.session = session


class ApplicationBuilder:
    def __init__(self, session):
        self.account = MainAccountant(session)
        self.account._income = 0
        self.account._expenses = 0
        self.account._expense_list = []
        self.account._expense_name = []
        self.account._income_name = []
        self.account._income_list = []

        self.prompt_income()

    def income_ask(self, add_income):
        self.account._add_income = add_income
        # add_income = input('Add income? [y/n]: ')
        return self  # add_income

    def income_sum(self):
        self.account._income = sum(self.income_list)
        return self  # there was no self

    def expense_ask(self, add_expense):
        self.account._add_expense = add_expense  # input('Add expense? [y/n]: ')
        return self  # add_expense

    def expense_sum(self):
        self.account._expenses = sum(self.expense_list)
        return self  # there was no self

    def income_check(self):
        if not self.account._income_list:
            # print('Please enter atleast one source of income. ')
            self.prompt_income()
        else:
            return self  # was just return

    def expense_check(self):
        if not self.account._expense_list:
            # print('Please enter atleast one expense. ')
            self.prompt_expense()
        else:
            return self  # was just return

    def prompt_income(self, income_list, income_name):
        x = False
        while not x:
            result = income_ask()
            if result == 'y':
                income_input = income_list  # int(input('Enter source of income. [Numbers Only]: '))
                self.account._income_list.append(income_input)
                income_name = income_name  # input('Enter income name. [Name Only]: ')
                self.account._income_name.append(income_name)
            else:
                self.income_check()
                x = True
        self.income_sum()
        name = [name for name in self.account._income_name]
        income = [income for income in self.account._income_list]
        incomedict = dict(zip(name, income))
        for k in incomedict:
            print(k + ': ', '$' + str(incomedict[k]))
        print('Total user income: ', '$' + str(self.income))
        self.prompt_expense()

    def prompt_expense(self, expense_input, expense_name):
        x = False
        while not x:
            result = self.expense_ask()
            if result == 'y':
                # self.expense_input = expense_input  # int(input('Enter expense amount. [Numbers Only]: '))
                self.account._expense_list.append(expense_input)
                # self.expense_name = expense_name  # input('Enter expense name. [Name Only]: ')
                self.account._expense_name.append(expense_name)
            else:
                self.expense_check()
                x = True
        self.expense_sum()
        name = [name for name in self.account._expense_name]
        expense = [income for income in self.account._expense_list]
        expensedict = dict(zip(name, expense))
        for k in expensedict:
            print(k + ': ', '$' + str(expensedict[k]))
        print('Total user expenses: ', '$' + str(self.account._expenses))
        self.user_value()

    def user_value(self):
        valoutput = self.income - self.expenses
        if valoutput < 0:
            print('You are in the negative, you have a deficit of ' + '$' + str(valoutput))
        if valoutput == 0:
            print('You have broken even, you are spending exactly as much as you make.')
        if valoutput > 0:
            print('You are in the positive, you have a surplus of ' + '$' + str(valoutput))
        # another = input('Would you like to run another analysis? [y/n]: ')
        # if another == 'y':
        #     self.reset_program()
        # else:
        #     self.close_program()

    # def reset_program(self):
    #     self.income = 0
    #     self.expenses = 0
    #     del self.expense_list[0:]
    #     del self.expense_name[0:]
    #     del self.income_name[0:]
    #     del self.income_list[0:]
    #     self.prompt_income()

    def build(self):
        return self.message

    # def close_program(self):
    #     print('Exiting Program.')
    #     sys.exit(0)


class Analyzer:
    def start_analyze(session):
        result = MainAccountant(session).income_ask(10000)

            # \
            # from_addr('me').to_addr('you').cc_addr('someone'). \
            # subject('test').body('hello'). \
            # build()

        return f'{result.session}'


if __name__ == '__main__':
    Analyzer()
