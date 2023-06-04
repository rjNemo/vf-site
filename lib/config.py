import json
from typing import TypedDict


class Config(TypedDict):
    name: str
    templatesFolder: str
    templates: list[str]
    staticFiles: list[str]
    outDir: str


def load() -> Config:
    with open("config.json", "r") as f:
        return json.loads(f.read())
