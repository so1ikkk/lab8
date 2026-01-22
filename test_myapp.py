import unittest
from jinja2 import Environment, PackageLoader, select_autoescape

from models import Author, App, User, Currency
from utils.currencies_api import get_currencies


# 1. Тестирование моделей
class TestModels(unittest.TestCase):

    def test_author(self):
        a = Author("Владислав", "P3124")
        self.assertEqual(a.name, "Владислав")
        self.assertEqual(a.group, "P3124")
        with self.assertRaises(ValueError):
            a.name = ""
        with self.assertRaises(ValueError):
            a.group = "123"

    def test_user(self):
        u = User(1, "Ярослав")
        self.assertEqual(u.id, 1)
        self.assertEqual(u.name, "Ярослав")
        with self.assertRaises(ValueError):
            u.id = -1
        with self.assertRaises(ValueError):
            u.name = "A"

    def test_currency(self):
        c = Currency(None, None, "USD", "Dollar", 92.5, 1)
        self.assertEqual(c.char_code, "USD")
        self.assertEqual(c.value, 92.5)
        self.assertEqual(c.nominal, 1)
        with self.assertRaises(ValueError):
            c.value = -1
        with self.assertRaises(ValueError):
            c.char_code = "US"


# 2. Тестирование функции get_currencies
class TestGetCurrencies(unittest.TestCase):

    def test_get_currencies_live(self):
        # Берём реальные курсы с сайта ЦБ РФ
        codes = ['USD', 'EUR', 'GBP']
        result = get_currencies(codes)
        for code in codes:
            self.assertIn(code, result)
            self.assertIsInstance(result[code], float)


# 3. Тестирование шаблонов Jinja2
class TestTemplates(unittest.TestCase):

    def setUp(self):
        # Инициализация Jinja2
        self.env = Environment(
            loader=PackageLoader('myapp'),
            autoescape=select_autoescape()
        )

        # Модели для шаблонов
        self.main_author = Author('Владислав Иголкин (504623)', 'P3124')
        self.app_info = App('Клиент-серверное приложение на Python', '1.0', self.main_author)
        self.users = [
            User(1, 'Ярослав'),
            User(2, 'Виктория'),
            User(3, 'Антон')
        ]
        self.currencies = [
            Currency(None, None, "USD", "Dollar", 92.5, 1),
            Currency(None, None, "EUR", "Euro", 101.2, 1),
            Currency(None, None, "GBP", "Pound", 118.3, 1)
        ]

    def test_index_template(self):
        template = self.env.get_template('index.html')
        html = template.render(
            myapp=self.app_info.name,
            author_name=self.main_author.name,
            group=self.main_author.group,
            navigation=[{'caption': 'Главная', 'href': '/'}]
        )
        self.assertIn('Владислав Иголкин', html)
        self.assertIn('Клиент-серверное приложение на Python', html)

    def test_users_template(self):
        template = self.env.get_template('users.html')
        html = template.render(users=self.users)
        self.assertIn('Ярослав', html)
        self.assertIn('Виктория', html)
        self.assertIn('Антон', html)

    def test_currencies_template(self):
        template = self.env.get_template('currencies.html')
        html = template.render(currencies=self.currencies)
        self.assertIn('USD', html)
        self.assertIn('EUR', html)
        self.assertIn('GBP', html)

# Запуск тестов
if __name__ == "__main__":
    unittest.main()
