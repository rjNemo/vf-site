build:
	pipenv run python main.py > index.html


run: build
	pipenv run python -m http.server