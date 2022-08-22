from jinja2 import FileSystemLoader
from jinja2.environment import Environment
from application.settings import TEMPLATE_DIR


def render(template_name, folder=TEMPLATE_DIR, **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)
