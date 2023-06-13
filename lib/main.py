import os
import shutil
import sys

from loguru import logger

from lib.config import load
from lib.engine import FileSystemRenderer


def main():
    try:
        config = load()
    except FileNotFoundError:
        logger.error("The configuration file 'config.json' was not found. Please verify it exists at the root level")
        sys.exit()

    data = {}
    destination_path = config.out_dir
    fs = FileSystemRenderer(config.templates_dir)

    logger.info(f"🏁 Start building {config.name}")

    if os.path.exists(destination_path) and os.path.isdir(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)

    for template in config.templates:
        logger.info(f"📃Render '{template}'")
        with open(os.path.join(destination_path, template), "w") as f:
            f.write(fs.render(template, data.get(template)))

    logger.info("⏩ Start copying staticfiles to build")
    for folder in config.static_files_dir:
        shutil.copytree(folder, os.path.join(config.out_dir, folder))

    logger.info("🎉 Done…")


if __name__ == "__main__":
    main()
