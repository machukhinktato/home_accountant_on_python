from index import index_view
from about import about_view
from create_view import create_view


class Application:
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        post = environ['REQUEST_METHOD']

        if path in self.urls:
            if post == 'POST':
                return [post.encode(encoding='utf-8')]
            view = self.urls[path]
            code, text = view()
            start_response(code, [('Content-Type', 'text/html')])
            return [text.encode(encoding='utf-8')]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b'Not Found']


post = []
urls = {
    '/': index_view,
    '/about': about_view,
    '/create': create_view
}

application = Application(urls)
