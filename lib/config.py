import json
from dataclasses import dataclass

NAME = "name"
TEMPLATES = "templates"
TEMPLATES_DIR = "templatesDir"
STATIC_FILES_DIR = "staticFilesDir"
OUT_DIR = "outDir"


@dataclass(frozen=True)
class Config:
    name: str
    static_files_dir: list[str]
    out_dir: str
    templates_dir: str


def load() -> Config:
    with open("config.json", "r") as f:
        raw_config = json.loads(f.read())
        return Config(
            name=raw_config[NAME],
            static_files_dir=raw_config[STATIC_FILES_DIR],
            out_dir=raw_config.setdefault(OUT_DIR, "dist"),
            templates_dir=raw_config.setdefault(TEMPLATES_DIR, "templates"),
        )
