from os import path

from loguru import logger

from lib.config import load
from lib.engine import render


def main():
    config = load()
    logger.info("🏁 Start building site")
    for template in config["templates"]:
        logger.info(f"📃Render '{template}'")
        with open(path.join(config["outDir"], template), "w") as f:
            f.write(render(template))
    logger.info("🎉 Done…")


if __name__ == "__main__":
    main()
