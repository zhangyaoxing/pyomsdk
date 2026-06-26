VENV_DIR ?= .venv
PYTHON ?= $(if $(wildcard $(VENV_DIR)/bin/python),$(VENV_DIR)/bin/python,python3)
PIP ?= $(PYTHON) -m pip

.PHONY: venv install install-dev lint test check docs clean

venv:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/python -m pip install --upgrade pip setuptools wheel

install: venv
	$(PIP) install -e .

install-dev: venv
	$(PIP) install -e .[dev]

lint:
	$(PYTHON) -m pylint src tests

test:
	$(PYTHON) -m pytest -q

check: lint test

docs:
	$(PYTHON) -c "import os, pkgutil, subprocess, sys; sys.path.insert(0, os.path.abspath('src')); import pyomsdk; modules = ['pyomsdk'] + sorted(m.name for m in pkgutil.walk_packages(pyomsdk.__path__, pyomsdk.__name__ + '.')); subprocess.run([sys.executable, '-m', 'pdoc', '--docformat', 'markdown', '--no-show-source', '--output-dir', 'docs', *modules], check=True); print(f'generated {len(modules)} html files')"

clean:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
