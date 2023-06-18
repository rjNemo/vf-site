import os
import shutil
import sys
import tomllib

from loguru import logger

from lib.config import load
from lib.engine import FileSystemRenderer


def main():
    try:
        config = load()
    except FileNotFoundError:
        logger.error("The configuration file 'config.json' was not found. Please verify it exists at the root level")
        sys.exit()

    destination_path = config.out_dir
    fs = FileSystemRenderer(config.templates_dir)

    logger.info(f"🏁 Start building {config.name}")

    clean_dist(destination_path)

    pages = [page for page in os.scandir("./pages") if page.is_file()]
    for page in pages:
        with open(page, "rb") as f:
            data = tomllib.load(f)
            logger.info(f"📃Render '{page.name}'")
            with open(os.path.join(destination_path, f'{data["name"]}.html'), "w") as fd:
                fd.write(fs.render(data["template"], data))

    logger.info("⏩ Start copying staticfiles to build")
    for folder in config.static_files_dir:
        shutil.copytree(folder, os.path.join(config.out_dir, folder))

    logger.info("🎉 Done…")


def clean_dist(destination_path: str):
    if os.path.exists(destination_path) and os.path.isdir(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)


if __name__ == "__main__":
    main()
