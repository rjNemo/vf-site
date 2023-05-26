build:
	pipenv run python main.py > dist/index.html


run: build
	cd dist && pipenv run python -m http.server