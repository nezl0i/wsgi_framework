from application.app import Framework
from application.settings import CURRENT_HOST, CURRENT_PORT
from views import routes
from wsgiref.simple_server import make_server
from application import settings


application = Framework(settings, routes)
# application = DebugApplication(settings, routes)
# application = FakeApplication(settings, routes)


with make_server(CURRENT_HOST, CURRENT_PORT, application) as httpd:
    print(f"Server running on {CURRENT_HOST}:{CURRENT_PORT}... \nhttp://{CURRENT_HOST}:{CURRENT_PORT}")
    httpd.serve_forever()
