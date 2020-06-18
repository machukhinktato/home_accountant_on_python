class Application:

    def __init__(self, urls, middlewares):
        self.urls = urls
        self.middlewares = middlewares

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        request = {}

        for middleware in self.middlewares:
            middleware(request)

        if path in self.urls:
            view = self.urls[path]
            code, text = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [text.encode(encoding='utf-8')]
        else:
            start_response('404 WHAT HAPPEND', [('Content-Type', 'text/plain')])
            return [b'Not Found']


# Установка
# pip install uwsgi

# Запуск
# uwsgi --http :8000 --wsgi-file simple_wsgi_server.py
def index_view(request):
    return '200 OK', 'Torpedo Moscow CHAMPION!!!'


def about_view(request):
    if 'secret' in request:
        return '200 OK', f'<h1>About Page {request["secret"]}</h1>'
    return '200 OK', f'<h1>About Page</h1>'


urls = {
    '/': index_view,
    '/about/': about_view
}


def secret_middleware(request):
    request['secret'] = 'secret'


# middlewares = [secret_middleware]
middlewares = []

application = Application(urls, middlewares)
