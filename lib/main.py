import os
import shutil
import sys
import tomllib
from distutils.dir_util import copy_tree

from loguru import logger

from lib.config import load
from lib.engine import FileSystemRenderer


def main():
    try:
        config = load()
    except FileNotFoundError:
        logger.error("The configuration file 'config.toml' was not found. Please verify it exists at the root level")
        sys.exit()

    destination_path = config.out_dir
    fs = FileSystemRenderer(config.templates_dir)

    logger.info(f"🏁 Start building {config.name}")

    clean_dist(destination_path)

    for page in os.scandir(config.templates_dir):
        if page.is_file():
            with open(os.path.join(destination_path, page.name), "w") as fd:
                data_file_path = os.path.join(config.data_dir, f"{page.name.split('.')[0]}.toml")
                data = {}
                if os.path.isfile(data_file_path):
                    with open(data_file_path, "rb") as f:
                        data = tomllib.load(f)
                        logger.debug(data)
                logger.info(f"📃Render '{page.name}'")
                fd.write(fs.render(page.name, data))

    logger.info("⏩ Start copying staticfiles to build")
    copy_tree(config.static_dir, os.path.join(config.out_dir))

    logger.info("🎉 Done…")


def clean_dist(destination_path: str):
    if os.path.exists(destination_path) and os.path.isdir(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)


if __name__ == "__main__":
    main()
