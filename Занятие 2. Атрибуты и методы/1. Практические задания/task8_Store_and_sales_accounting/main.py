from typing import Optional


class Product:
    """
    Классовые атрибуты для отслеживания общей информации
        total_products(число): Отслеживает общее количество товаров на складе.
        total_revenue(число): Хранит общую выручку от продаж.
    """
    total_products = 0
    total_revenue = 0.0

    def __init__(self, name: str, price: int | float, quantity: int):
        """
        :param name: Название товара
        :param price: Цена товара
        :param quantity: Количество товара на складе
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.add_value_total_products(quantity)

    @classmethod
    def add_value_to_total_revenue(cls, value):
        cls.total_revenue += value

    @classmethod
    def add_value_total_products(cls, value):
        cls.total_products += value


    def sell(self, amount: int) -> None:
        """
        Уменьшает количество товара на указанное значение, обновляет выручку.
        Если количество товара недостаточно, метод должен сообщить об этом, вызвав raise ValueError.
        :param amount: Количество проданного товара
        :return:
        """
        if amount > self.quantity:
            raise ValueError(f"Недостаточно товара {self.name} на складе!")
        self.quantity -= amount
        revenue = amount * self.price
        self.add_value_to_total_revenue(revenue)
        self.add_value_total_products(-amount)
        print(f"Продано {amount} шт. товара {self.name}. Выручка: {revenue:.2f}")

    def restock(self, amount: int) -> None:
        """
        Увеличивает количество товара на указанное значение
        :param amount: Количество добавляемого товара
        :return:
        """
        self.quantity += amount
        self.add_value_total_products(amount)
        print(f"Поступило {amount} шт. товара {self.name}. Всего на складе: {self.quantity}")

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


class Store:
    def __init__(self, name: str, products: Optional[list[Product]] = None):
        self.name = name
        self.products = products if products is not None else []

    def total_inventory(self):
        """
        Возвращает общее количество всех товаров в магазине.
        :return:
        """
        return sum(product.quantity for product in self.products)

    def total_value(self):
        """
        Возвращает общую стоимость всех товаров в магазине.
        :return:
        """
        return sum(product.price * product.quantity for product in self.products)

    @staticmethod
    def compare_prices(product1: Product, product2: Product):
        if product1.price > product2.price:
            return product1.name
        elif product1.price < product2.price:
            return product2.name
        else:
            return "Цены одинаковы"


if __name__ == "__main__":
    apple = Product("Apple", 1.5, 100)
    banana = Product("Banana", 0.9, 150)
    cherry = Product("Cherry", 3.0, 50)

    store = Store("My Grocery Store", [apple, banana, cherry])

    print(store.total_inventory())  # Вывод: 300
    print(store.total_value())  # Вывод: 435.0

    apple.sell(30)
    print(Product.total_revenue)  # Вывод: 45.0

    print(Store.compare_prices(apple, banana))  # Вывод: Apple

    print(store.total_inventory())  # Вывод: 270
    print(store.total_value())  # Вывод: 390.0
