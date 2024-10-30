.PHONY: init
init:
	uv sync

.PHONY: run
run:
	uv run python app.py

.PHONY: fix
fix:
	uv run ruff format
