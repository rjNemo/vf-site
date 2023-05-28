import sys
from os import path

from loguru import logger

from lib.config import load
from lib.engine import render


def main():
    try:
        config = load()
    except FileNotFoundError:
        logger.error("The configuration file 'config.json' was not found. Please verify it exists at the root level")
        sys.exit()

    logger.info(f"🏁 Start building {config['name']}")
    for template in config["templates"]:
        logger.info(f"📃Render '{template}'")
        with open(path.join(config["outDir"], template), "w") as f:
            f.write(render(template, data.get(template)))
    logger.info("🎉 Done…")


if __name__ == "__main__":
    main()
