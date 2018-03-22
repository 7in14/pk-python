SHELL := /bin/zsh

default: build

init: setup virt build

build: install test

# Run tests with coverage
test:
	pytest -v -s --cov-report xml:coverage.xml --cov=app

# Install dependencies
install:
	pip3 install -r requirements.txt

# Save all dependencies
save:
	pipreqs . --force

# Run this once
setup:
	pip3 install pipreqs pytest pytest-cov

# Setup virtual environment
virt:
	pip3 install virtualenv
	virtualenv -p /usr/local/Cellar/python3/3.6.4_2/bin/python3.6 venv
	source ./venv/bin/activate

run:
	export FLASK_DEBUG=1
	python app.py
