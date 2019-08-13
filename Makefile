install:
	python setup.py install

help: install
	ascii-grid-to-png --help

run_tests:
	python -m pytest tests/

lint:
	flake8 ascii_grid_to_png tests
