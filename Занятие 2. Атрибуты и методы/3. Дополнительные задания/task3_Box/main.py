class Box:
    def __init__(self):
        self.items = set()  # Используем множество для хранения уникальных элементов

    def __contains__(self, item):
        print("Вызов Box.__contains__")
        return item in self.items

    def __iter__(self):
        print("Вызов Box.__iter__")
        return iter(self.items)

    def __len__(self):
        print("Вызов Box.__len__")
        return len(self.items)

    def __repr__(self):
        return f"Box({list(self.items)})"

    def __add__(self, item):
        print("Вызов Box.__add__")
        self.items.add(item)
        return self


if __name__ == "__main__":
    box = Box()

    # Добавляем элементы в коробку
    box += "apple"
    box += "banana"
    box += "orange"
    box += "apple"  # Дубликаты не добавляются

    # Проверяем количество элементов в коробке
    print(f"Количество элементов в коробке: {len(box)}")  # 3

    # Проверка наличия элемента
    if "banana" in box:
        print("Банан есть в коробке")

    # Итерация по элементам коробки
    for item in box:
        print(item)

    # Вывод коробки
    print(box)  # Box(['apple', 'banana', 'orange'])
