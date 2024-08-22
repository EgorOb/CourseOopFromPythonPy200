class MyClass:
    def __init__(self, value):
        self.value = value  # Открытый атрибут
        self._value = value  # Защищённый атрибут
        self.__value = value  # Приватный атрибут

    def my_method(self):  # Открытый метод
        return self.value

    def _my_method(self):  # Защищённый метод
        return self._value

    def __my_method(self):  # Приватный метод
        return self.__value


if __name__ == "__main__":
    obj = MyClass(42)

    print(obj.value)  # Открытый доступ
    obj.value = 100  # Изменение атрибута

    print(obj._value)  # Можно получить доступ, но это нарушает соглашение
    obj._value = 100  # Возможное изменение, но не рекомендуется

    try:
        print(obj.__value)  # Ошибка, доступ невозможен напрямую
    except AttributeError as err:
        print(err)
    try:
        obj.__my_method()  # Ошибка, доступ невозможен напрямую
    except AttributeError as err:
        print(err)

    # Однако, есть обходной путь (механизм манглинга):
    print(obj._MyClass__value)  # Доступ возможен через манглинг имен, но это очень не рекомендуется
