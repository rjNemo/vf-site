from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())
template = env.get_template("index.html")
print(template.render())
