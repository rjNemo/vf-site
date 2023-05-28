from os import path

from jinja2 import Environment, FileSystemLoader, select_autoescape

engine = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(),
)


def render(template: str) -> str:
    return engine.get_template(template).render()


# TODO: from a config
templates = ["index.html", "t2-corail.html", "t3-azur.html", "contact.html"]


for template in templates:
    print(f"render '{template}'")
    with open(path.join("dist", template), "w") as f:
        f.write(render(template))
