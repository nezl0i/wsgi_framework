from krosha_framework.frame import GetRequests, PostRequests


class PageNotFound404:
    def __call__(self, request):
        return '404 NotFound', '404 Not Found'


class Framework:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):

        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}

        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get(environ)
            request['data'] = data

            print(f'POST requests: {data}')

            if path == '/contact/':
                email = data.get('email', None)
                theme = data.get('theme', None)
                message = data.get('comment', None)
                with open('message.txt', 'w', encoding='utf-8') as file:
                    file.write(f'Email: {email}\nTheme: {theme}\nMessage: {message}')

        if method == 'GET':
            request_params = GetRequests().get(environ)
            request['request_params'] = request_params

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        for front in self.fronts:
            front(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


class DebugApp(Framework):

    def __init__(self, routes, fronts):
        self.application = Framework(routes, fronts)
        super().__init__(routes, fronts)

    def __call__(self, env, response):
        print('DEBUG MODE')
        print(env)
        return self.application(env, response)


class FakeApp(Framework):

    def __init__(self, routes, fronts):
        self.application = Framework(routes, fronts)
        super().__init__(routes, fronts)

    def __call__(self, env, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake']

