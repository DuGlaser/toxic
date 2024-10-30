UV := ./.uv/bin/uv

.PHONY: init
init: .uv
	$(UV) sync

.PHONY: run
run: .uv
	$(UV) run python app.py

.PHONY: fix
fix: .uv
	$(UV) run ruff format

.uv:
	curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="./.uv" INSTALLER_NO_MODIFY_PATH=1 sh
