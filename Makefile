.PHONY: tests
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

BROWSER := python -c "$$BROWSER_PYSCRIPT"



install:
	python setup.py install

help: install
	ascii-grid-to-png --help

tests:
	python -m pytest tests/

lint:
	flake8 ascii_grid_to_png tests

coverage:
	coverage run --source ascii_grid_to_png -m pytest tests/
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html
