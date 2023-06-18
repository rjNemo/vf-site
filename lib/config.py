import tomllib
from dataclasses import dataclass

NAME = "name"
TEMPLATES_DIR = "templates_dir"
STATIC_FILES = "static_files"
OUT_DIR = "out_dir"


@dataclass(frozen=True)
class Config:
    name: str
    static_files: list[str]
    out_dir: str
    templates_dir: str


def load() -> Config:
    with open("config.toml", "rb") as f:
        raw_config = tomllib.load(f)
        return Config(
            name=raw_config[NAME],
            static_files=raw_config[STATIC_FILES],
            out_dir=raw_config.setdefault(OUT_DIR, "dist"),
            templates_dir=raw_config.setdefault(TEMPLATES_DIR, "templates"),
        )
