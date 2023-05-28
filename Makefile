build:
	pipenv run python main.py


run: build
	cd dist && pipenv run python -m http.server
