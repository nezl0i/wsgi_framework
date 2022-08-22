from krosha_framework.app import Framework
from krosha_framework.settings import CURRENT_HOST, CURRENT_PORT, BASE_DIR
from urls import fronts
from views import routes
from wsgiref.simple_server import make_server


application = Framework(routes, fronts)

with make_server(CURRENT_HOST, CURRENT_PORT, application) as httpd:
    print(f"Server running on {CURRENT_HOST}:{CURRENT_PORT}... \nhttp://{CURRENT_HOST}:{CURRENT_PORT}")
    httpd.serve_forever()
