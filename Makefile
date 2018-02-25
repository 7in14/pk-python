default: build

build: install test

test:
	pytest -v -s --cov-report xml:coverage.xml --cov=app

install:
	pip3 install -r requirements.txt

save:
	pipreqs . --force

setup:
	pip3 install pipreqs pytest pytest-cov

virt:
	pip3 install virtualenv
	virtualenv -p /usr/local/Cellar/python3/3.6.4_2/bin/python3.6 venv

virt-start:
	source ./venv/bin/activate

run:
	export FLASK_DEBUG=1
	python app.py
