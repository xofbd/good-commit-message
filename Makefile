POETRY_RUN := poetry run
POETRY_EXPORT := poetry export --without-hashes -f requirements.txt
SHELL := /bin/bash

.PHONY: all
all: clean install

# Installing
.make.install: poetry.lock
	poetry install --no-dev
	touch $@

.PHONY: install
install: .make.install

.make.install-dev: poetry.lock
	poetry install
	touch $@

.PHONY: install-dev
install-dev: .make.install-dev

# Virtual environment
poetry.lock: pyproject.toml
	poetry lock
	touch $@

requirements-dev.txt: poetry.lock
	$(POETRY_EXPORT) --dev -o $@

.PHONY: up-to-date
up-to-date:
	touch pyproject.toml
	touch poetry.lock
	touch requirements-dev.txt
	touch --no-create .make.install-dev

# Testing
.PHONY: test-lint
test-lint: | .make.install-dev
	$(POETRY_RUN) flake8 --config=pyproject.toml gcm tests

.PHONY: test-unit
test-unit: | .make.install-dev
	$(POETRY_RUN) pytest -s --cov=gcm --cov-report=term --cov-report=xml

.PHONY: tests
tests: test-lint test-unit

.PHONY: tox
tox: | .make.install-dev
	$(POETRY_RUN) tox

# Utilities
.PHONY: clean
clean:
	find . | grep [py]cache | xargs rm -rf
	rm -f .coverage coverage.xml .make.*
	rm -rf .tox
