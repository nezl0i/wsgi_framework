from jinja2 import FileSystemLoader, Environment
from application.settings import TEMPLATE_DIR


def render(template_name, folder=TEMPLATE_DIR, static_url='/static/', **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    env.globals['static'] = static_url
    template = env.get_template(template_name)
    return template.render(**kwargs)
