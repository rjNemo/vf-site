build:
	@pipenv run python -m lib.main


run: build
	@cd dist && pipenv run python -m http.server

lint:
	@pipenv run black .
	@pipenv run ruff .
	@pipenv run mypy .
