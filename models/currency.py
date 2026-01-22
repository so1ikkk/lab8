class Currency:
    def __init__(
        self,
        id: int | None,
        num_code: str | None,
        char_code: str,
        name: str | None,
        value: float,
        nominal: int
    ):
        self.id = id
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal

    @property
    def char_code(self):
        return self.__char_code

    @char_code.setter
    def char_code(self, value: str):
        if isinstance(value, str) and len(value) == 3:
            self.__char_code = value
        else:
            raise ValueError('Ошибка при задании символьного кода валюты')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self.__value = float(value)
        else:
            raise ValueError('Ошибка при задании курса валюты')

    @property
    def nominal(self):
        return self.__nominal

    @nominal.setter
    def nominal(self, value: int):
        if isinstance(value, int) and value > 0:
            self.__nominal = value
        else:
            raise ValueError('Ошибка при задании номинала валюты')

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value is None or isinstance(value, int):
            self.__id = value
        else:
            raise ValueError('Ошибка при задании id валюты')

    @property
    def num_code(self):
        return self.__num_code

    @num_code.setter
    def num_code(self, value):
        if value is None or isinstance(value, str):
            self.__num_code = value
        else:
            raise ValueError('Ошибка при задании цифрового кода валюты')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is None or isinstance(value, str):
            self.__name = value
        else:
            raise ValueError('Ошибка при задании названия валюты')
