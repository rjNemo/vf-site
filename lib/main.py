from os import path

from loguru import logger

from lib.config import load_templates
from lib.engine import render


def main():
    logger.info("🏁 Start building site")
    for template in load_templates():
        logger.info(f"📃Render '{template}'")
        with open(path.join("dist", template), "w") as f:
            f.write(render(template))
    logger.info("🎉 Done…")


if __name__ == "__main__":
    main()
