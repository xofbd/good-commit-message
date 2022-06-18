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

# Testing
.PHONY: test-lint
test-lint: | .make.install-dev
	$(POETRY_RUN) flake8 --config=pyproject.toml gcm tests

.PHONY: test-unit
test-unit: | .make.install-dev
	$(POETRY_RUN) pytest -s --cov=gcm

.PHONY: tests
tests: test-lint test-unit

# Utilities
.PHONY: clean
clean:
	find . | grep [py]cache | xargs rm -rf
	rm -f .coverage coverage.xml .make.*
