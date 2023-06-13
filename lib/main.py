import os
import shutil
import sys

from loguru import logger

from lib.config import load
from lib.engine import FileSystemRenderer

NAME = "name"
TEMPLATES = "templates"
TEMPLATES_DIR = "templatesDir"
STATIC_FILES_DIR = "staticFilesDir"
OUT_DIR = "outDir"


def main():
    try:
        config = load()
    except FileNotFoundError:
        logger.error("The configuration file 'config.json' was not found. Please verify it exists at the root level")
        sys.exit()

    data = {}
    destination_path = config[OUT_DIR]
    fs = FileSystemRenderer(config.setdefault(TEMPLATES_DIR, TEMPLATES))

    logger.info(f"🏁 Start building {config[NAME]}")

    if os.path.exists(destination_path) and os.path.isdir(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)

    for template in config[TEMPLATES]:
        logger.info(f"📃Render '{template}'")
        with open(os.path.join(destination_path, template), "w") as f:
            f.write(fs.render(template, data.get(template)))

    logger.info("⏩ Start copying staticfiles to build")
    for folder in config[STATIC_FILES_DIR]:
        shutil.copytree(folder, os.path.join(config[OUT_DIR], folder))

    logger.info("🎉 Done…")


if __name__ == "__main__":
    main()
