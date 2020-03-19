poetry-outdated:
	poetry show --outdated

poetry-update:
	poetry update

poetry-export-requirements:
	poetry export -f requirements.txt > requirements.txt

poetry-test:
	poetry run pytest
