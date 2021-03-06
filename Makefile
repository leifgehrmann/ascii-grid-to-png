.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

poetry-outdated:
	poetry show --outdated

poetry-update:
	poetry update

poetry-export-requirements: ## Export poetry lockfile to requirements.txt
	poetry export -f requirements.txt > requirements.txt

test:
	poetry run pytest

lint: ## check style with flake8
	poetry run flake8 ascii_grid_to_png tests

coverage: ## check code coverage quickly with the default Python
	poetry run coverage run --source ascii_grid_to_png -m pytest
	poetry run coverage report -m

coverage-html: coverage ## check code coverage quickly with the default Python
	poetry run coverage html
	$(BROWSER) htmlcov/index.html
