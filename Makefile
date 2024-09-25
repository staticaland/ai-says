run:
	uv run hello.py

black:
	uvx black hello.py

ell:
	uv run ell-studio --storage logs

aider:
	uvx --from aider-chat aider

a: aider

PHONY: run black ell aider a