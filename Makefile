VENV_DIR ?= .venv
PYTHON ?= $(if $(wildcard $(VENV_DIR)/bin/python),$(VENV_DIR)/bin/python,python3)
PIP ?= $(PYTHON) -m pip

.PHONY: venv install install-dev lint test check clean

venv:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/python -m pip install --upgrade pip setuptools wheel

install:
	$(PIP) install -e .

install-dev:
	$(PIP) install -e .[dev]

lint:
	$(PYTHON) -m pylint src tests

test:
	$(PYTHON) -m pytest -q

check: lint test

clean:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
