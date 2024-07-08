class OwnerMagazineDecorator:
    @staticmethod
    def registration_owner(user):
        def add_product_to_magazine(user: User, magazine: Magazine, product: Product):
            if user.name != magazine.owner.name:
                print("У пользователя нет доступа к магазину!")
                return user
            magazine.add_product(product)
            return user

        def delete_product_from_magazine(self, magazine: Magazine, product: Product):
            if user.name != magazine.owner.name:
                print("У пользователя нет доступа к магазину!!")
                return user
            magazine.remove_product(product)
            return user

        user.add_product_to_magazine = add_product_to_magazine
        user.delete_product_from_magazine = delete_product_from_magazine


class Cart:
    products_cart = list()

    def add_to_cart(self, product):
        self.products_cart.append(product)

    def del_from_cart(self, product_name: str):
        for prod in self.products_cart:
            if product_name == prod.name:
                self.products_cart.remove(prod)
                print("Продукт удален!")

    def order_and_pay(self):
        self.products_cart.clear
        print("Заказ обработан, корзина пуста!")


class User:
    id: int
    name: str
    cart: Cart
    client_session= None

    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id
        self.cart = Cart()

    # session maker
    def start_session(self):
        self.client_session = Session(self)
        return self

    def end_session(self):
        del self.client_session

    def change_magazine(self, magazine_name, market_place):
        for magazine in market_place.magazines:
            if magazine.name == magazine_name:
                self.client_session.magazine = magazine
        return self
    
    def add_to_cart(self, product_name):
        for prod in self.client_session.magazine.products:
            if product_name == prod.name:
                self.cart.add_to_cart(prod)
                print("Добавили продукт в корзину!")
        return self

    def remove_from_cart(self, product_name: str):
        self.cart.del_from_cart(product_name)
        return self

    def order_products(self):
        self.cart.order_and_pay()
        return self


class Product:
    id: int
    name: str
    price: float
    category: str

    def __init__(self, name: str, price: float, category: str = None) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.id = id


class Magazine:
    name: str
    owner: User
    products = list()

    def add_product(self, product):
        self.products.append(product)
        print("Добавили продукт в магазин!")
    
    def remove_product(self, product: Product):
        for prod in self.products:
            if product.name == prod.name:
                self.products.pop(prod)
                print("Продукт удален успешно!")


class MarketPlace:
    __count = 1
    magazines = list()
    users = list()

    def registration(self, name):
        user = User(name, self.__count)
        self.users.append(user)
        self.__count += 1
        return user

    def registration_magazine(self, user, name_magazine):
        magazine = Magazine()
        magazine.name = name_magazine
        magazine.owner = user
        OwnerMagazineDecorator.registration_owner(user)
        self.magazines.append(magazine)
        return magazine


class Session:
    magazine: Magazine = None
    user = None

    def __init__(self, user):
        self.user = user


alieExpress = MarketPlace()

user1 = alieExpress.registration("user1")
user2 = alieExpress.registration("user2")

magazine = alieExpress.registration_magazine(user1, "clothes")

user1.start_session().add_product_to_magazine(user1, magazine, Product("t-shirt", 70.0)).end_session()
user1.start_session().add_product_to_magazine(user1, magazine, Product("shirt", 80.0)).end_session()
user1.start_session().order_products().end_session()


user1.start_session().change_magazine("clothes", alieExpress).add_to_cart("shirt").end_session()
user2.start_session().change_magazine("clothes", alieExpress).add_to_cart("shirt").remove_from_cart("shirt").end_session()

