Ранее рассматривали, что системный атрибут `__class__` содержит в себе класс, экземпляром которого он является.

А в `__repr__` мы прописывали название класса, можно немного стандартизировать запись, чтобы не прописывать название класса,
так как оно есть в `__class__.__name__`

С помощью `self.__class__.__name__` перепишите приведенный участок кода в `__repr__` 