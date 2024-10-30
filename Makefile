.PHONY: init
init:
	uv sync

run:
	uv run python app.py

fix:
	uv run ruff format
