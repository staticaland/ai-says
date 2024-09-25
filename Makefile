run:
	uv run hello.py

ruff:
	uvx ruff format hello.py

lint:
	uvx ruff check

ell:
	uv run ell-studio --storage logs

aider:
	uvx --from aider-chat aider

a: aider

black: ruff


PHONY: run black ell aider a