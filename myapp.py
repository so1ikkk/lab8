from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from jinja2 import Environment, PackageLoader, select_autoescape

from models import Author, App, User, Currency
from utils.currencies_api import get_currencies


# Jinja2 Environment
env = Environment(
    loader=PackageLoader('myapp'),
    autoescape=select_autoescape()
)

template_index = env.get_template('index.html')
template_users = env.get_template('users.html')
template_currencies = env.get_template('currencies.html')


# Модели
main_author = Author('Владислав Иголкин (504623)', 'P3124')
app_info = App('Клиент-серверное приложение на Python', '1.0', main_author)

users = [
    User(1, 'Ярослав'),
    User(2, 'Виктория'),
    User(3, 'Антон')
]

# HTTP Handler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()

        # Главная страница
        if path == '/':
            html = template_index.render(
                myapp=app_info.name,
                author_name=main_author.name,
                group=main_author.group,
                navigation=[
                    {'caption': 'Главная', 'href': '/'},
                    {'caption': 'Пользователи', 'href': '/users'},
                    {'caption': 'Валюты', 'href': '/currencies'}
                ]
            )

        # Список пользователей
        elif path == '/users':
            html = template_users.render(users=users)

        # Курсы валют
        elif path == '/currencies':
            codes = ['USD', 'EUR', 'GBP']
            data = get_currencies(codes)

            currencies = []
            for code, value in data.items():
                currencies.append(Currency(
                    id=None,
                    num_code=None,
                    char_code=code,
                    name=None,
                    value=value,
                    nominal=1
                ))

            html = template_currencies.render(currencies=currencies)

        # 404
        else:
            html = '<h1>404 - Страница не найдена</h1>'

        self.wfile.write(html.encode('utf-8'))

# ------------------------
# Запуск сервера
# ------------------------
if __name__ == '__main__':
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, Handler)
    print('Сервер запущен на http://localhost:8080')
    httpd.serve_forever()
