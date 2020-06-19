from index import index_view


class Application:
    def __init__(self, urls, middlewares):
        self.urls = urls
        self.middlewares = middlewares

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        # post = environ['POST']

        request = {}

        for middleware in self.middlewares:
            middleware(request)

        if path in self.urls:
            view = self.urls[path]
            code, text = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [text.encode(encoding='utf-8')]
        else:
            start_response('404 WHAT HAPPEND', [('Content-Type', 'text/html')])
            return [b'Not Found']


def about_view(request):
    if 'secret' in request:
        return '200 OK', f'<h1>About Page {request["secret"]}</h1>'
    return '200 OK', f'<h1>About Page</h1>'


urls = {
    '/': index_view,
    '/about': about_view
}


def secret_middleware(request):
    request['secret'] = 'secret or not'


middlewares = [secret_middleware]
# middlewares = []

application = Application(urls, middlewares)
