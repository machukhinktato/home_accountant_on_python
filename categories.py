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

