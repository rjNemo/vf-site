from jinja2 import Environment, FileSystemLoader, select_autoescape

engine = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())


def render(template: str, context: dict | None = None) -> str:
    return engine.get_template(template).render(context or {})
