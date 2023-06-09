build:
	@pipenv run python -m lib.main

run: build
	@echo ""
	@cd dist && pipenv run python -m http.server

lint:
	@pipenv run black .
	@pipenv run ruff . --fix
	@pipenv run mypy .
