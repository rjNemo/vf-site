from dataclasses import dataclass
from typing import Protocol

from jinja2 import Environment, FileSystemLoader, select_autoescape

engine = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())


class Renderer(Protocol):
    def render(self, template: str, context: dict | None = None) -> str:
        ...


@dataclass
class FileSystemRenderer(Renderer):
    path: str = "templates"

    def render(self, template: str, context: dict | None = None) -> str:
        return engine.get_template(template).render(context or {})
