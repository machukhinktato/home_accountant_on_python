def index_view():
    return '200 OK', 'Greetings from King Mike'


def about_view():
    return '200 OK', '<h1>King, since born</h1>'

urls = {
    '/': index_view(),
    '/about': about_view()
}


def application(environ, start_response):
    pass

class Application:
    def __init__(self, urls):
        self.urls = urls


    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if path == '/':
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [b'Hello from a King Mike, whom trying to be the best']
        elif path == 'about':
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [b"<h1> He's real king</h1>"]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"<h1> He's real king</h1>"]
