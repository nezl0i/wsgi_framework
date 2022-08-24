from os import path
from application.content import TYPES
from application.frame import GetRequests, PostRequests
from patterns.patterns import Logger

logger = Logger('app')


class PageNotFound404:
    def __call__(self, request):
        return '404 NotFound', '404 Not Found'


class Framework:

    def __init__(self, settings, routes):
        self.routes = routes
        self.settings = settings

    def __call__(self, environ, start_response):

        path_info = environ['PATH_INFO']

        if not path_info.endswith('/'):
            path_info = f'{path_info}/'

        request = {}

        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get(environ)
            request['data'] = data

            print(f'POST requests: {data}')
            if data.get('method'):
                method_new = data['method']
                if method_new != '':
                    request['method'] = data['method']

            if path_info == '/contact/':
                name = data.get('name')
                phone = data.get('phone')
                email = data.get('email')
                topic = data.get('topic')
                message = data.get('message')
                with open('message.txt', 'w', encoding='utf-8') as file:
                    file.write(f'Name: {name}\nEmail: {email}\nPhone: {phone}\nTopic: {topic}\nMessage: {message}')

        if method == 'GET':
            request_params = GetRequests().get(environ)
            request['request_params'] = request_params

        if path_info in self.routes:
            view = self.routes[path_info]
            content_type = self.get_content_type(path_info)
            code, body = view(request)
            body = body.encode('utf-8')
        elif path_info.startswith(self.settings.STATIC_URL):
            file_path = path_info[len(self.settings.STATIC_URL):len(path_info) - 1]
            content_type = self.get_content_type(file_path)
            code, body = self.get_static(self.settings.STATIC_FILES_DIR,
                                         file_path)
        else:
            view = PageNotFound404()
            content_type = self.get_content_type(path_info)
            code, body = view(request)
            body = body.encode('utf-8')

        start_response(code, [('Content-Type', content_type)])
        return [body]

    @staticmethod
    def get_content_type(file_path, content_types_map=TYPES):
        file_name = path.basename(file_path).lower()
        extension = path.splitext(file_name)[1]
        return content_types_map.get(extension, "text/html")

    @staticmethod
    def get_static(static_dir, file_path):
        path_to_file = path.join(static_dir, file_path)
        with open(path_to_file, 'rb') as f:
            file_content = f.read()
        status_code = '200 OK'
        return status_code, file_content


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

