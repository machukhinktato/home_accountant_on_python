import abc


class AbstractCategory(metaclass=abc.ABCMeta):
    def __init__(self):
        self.category = Categories()

    def post_income(self):
        pass

    def post_expense(self):
        pass


class Categories:
    title = {
        'products': Products,
        'entertaiment': Entertaiment,
        'municipal_services': MunicipalServices,
        'car': Car,
        'domestic_appliances': DomesticApp,
        'furniture': Furniture,
    }


class BaseCategoriesMixin:
    def __init__(self):
        self.title = title
        self.expenses = expenses


class Products(BaseCategoriesMixin, title):
    pass


class Entertaiment(BaseCategoriesMixin, title):
    pass


class MunicipalServices(BaseCategoriesMixin, title):
    pass


class Car(BaseCategoriesMixin, title):
    pass


class DomesticApp(BaseCategoriesMixin, title):
    pass


class Furniture(BaseCategoriesMixin, title):
    pass

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
