import os
import shutil
import sys
import tomllib
from distutils.dir_util import copy_tree
from time import perf_counter

from rich import print

from lib.config import Config, load
from lib.engine import FileSystemRenderer


def main():
    start = perf_counter()
    config = parse_config()

    fs = FileSystemRenderer(config)

    print(f"🏁 Start building [italic red]{config.name}[/italic red]")
    clean_dist(config.out_dir)

    for page in os.scandir(config.templates_dir):
        if page.is_file():
            with open(os.path.join(config.out_dir, page.name), "w") as fd:
                data = parse_data(page, config.data_dir)
                print(f"📃 Render [italic cyan]{page.name}[/italic cyan]")
                fd.write(fs.render(page.name, data))

    print("⏩  Copy static assets to build")
    copy_tree(config.static_dir, os.path.join(config.out_dir))

    end = perf_counter()
    print(f"🎉 Done… in [italic red]{(end - start) * 1000:.2f} ms[/italic red]")


def parse_config() -> Config:
    try:
        config = load()
    except FileNotFoundError:
        print(
            "🛑 configuration file [italic red]'config.toml'[/italic red] was not found. "
            "Please verify it exists at the root level"
        )
        sys.exit(1)
    else:
        return config


def parse_data(page: os.DirEntry, data_dir: str) -> dict:
    data_file_path = os.path.join(data_dir, f"{page.name.split('.')[0]}.toml")
    data = {}
    if os.path.isfile(data_file_path):
        with open(data_file_path, "rb") as f:
            data = tomllib.load(f)
    return data


def clean_dist(destination_path: str):
    if os.path.exists(destination_path) and os.path.isdir(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)


if __name__ == "__main__":
    main()
