def application(environ, start_response):
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