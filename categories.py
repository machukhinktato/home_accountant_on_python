import abc


class AbstractCategory(metaclass=abc.ABCMeta):
    def __init__(self):
        self.category = Category_format()

    def post_income(self):
        pass

    def post_expense(self):
        pass


class Categories:
    title = {
        'foodstuff': foodstuff,
        'alcohol': alcohol,
        'car': car,
        'entertaiment': entertaiment,
        'studies': studies,
        'products': products,
        'fines': fines,
        'furniture': furniture,
        'job': job,
        'utility_bills': utility_bills,
        'user_pick': {},
        }

    def add_category(self, categories, user_pick):
        categories = categories()
        user_pick = user_pick
        categories.title.update(user_pick=user_pick)
        return categories

    def del_category(self, categories, which_one):
        categories = categories()
        categories.user_pick.pop(which_one)
        return categories