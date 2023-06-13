from typing import Protocol

from jinja2 import Environment, FileSystemLoader, select_autoescape


class Renderer(Protocol):
    def render(self, template: str, context: dict | None = None) -> str:
        ...


class FileSystemRenderer(Renderer):
    def __init__(self, path: str):
        self.engine = Environment(loader=FileSystemLoader(path), autoescape=select_autoescape())

    def render(self, template: str, context: dict | None = None) -> str:
        return self.engine.get_template(template).render(context or {})
