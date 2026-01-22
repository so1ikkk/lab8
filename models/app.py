from .author import Author


class App:
    def __init__(self, name: str, version: str, author: Author):
        self.name = name
        self.version = version
        self.author = author

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) >= 2:
            self.__name = value
        else:
            raise ValueError('Ошибка при задании имени приложения')

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, value: str):
        if isinstance(value, str) and len(value) >= 1:
            self.__version = value
        else:
            raise ValueError('Ошибка при задании версии приложения')

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value: Author):
        if isinstance(value, Author):
            self.__author = value
        else:
            raise ValueError('author должен быть объектом Author')
