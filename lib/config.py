import json


def load_templates():
    with open("config.json", "r") as f:
        res = json.loads(f.read())
    return res["templates"]
