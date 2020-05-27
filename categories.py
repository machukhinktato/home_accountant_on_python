# import abc


# class AbstractCategory(metaclass=abc.ABCMeta):
#     pass
# def __init__(self):
#     self.category = Categories()
#
# def post_income(self):
#     pass
#
# def post_expense(self):
#     pass


class BaseCategoriesMixin:
    def __init__(self):
        self.title = ''
        se;f.expenses = []

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'


class Products(BaseCategoriesMixin):
    title = 'Продукты'



class Entertaiment(BaseCategoriesMixin):
    title = 'Развлечение'


class MunicipalServices(BaseCategoriesMixin):
    title = 'Коммунальные услуги'


class Car(BaseCategoriesMixin):
    title = 'Машина'


class DomesticApp(BaseCategoriesMixin):
    title = 'Бытовая техника'


class Furniture(BaseCategoriesMixin):
    title = 'Мебель'


class Categories:
    title = {
        'products': Products,
        'entertaiment': Entertaiment,
        'municipal_services': MunicipalServices,
        'car': Car,
        'domestic_appliances': DomesticApp,
        'furniture': Furniture,
    }

    # will be realized later
    # def add_category(self, categories, user_pick):
    #     categories = categories()
    #     user_pick = user_pick
    #     categories.title.update(user_pick=user_pick)
    #     return categories
    #
    # def del_category(self, categories, which_one):
    #     categories = categories()
    #     categories.user_pick.pop(which_one)
    #     return categories

# a = BaseCategoriesMixin('Дима', expense=5000)
# print(a)
