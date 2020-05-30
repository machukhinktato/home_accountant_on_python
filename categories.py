class BaseCategoriesMixin:
    def __init__(self):
        self.title = ''
        self.expenses = []

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
