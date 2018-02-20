default: build

build: install test

test:
	py.test --cov-report html:cov_html
        --cov-report xml:cov.xml
        --cov-report annotate:cov_annotate
        --cov=myproj tests/

install:
	pip3 install -r requirements.txt

save:
	pipreqs . --force

setup:
	pip3 install pipreqs pytest pytest-cov

venv:
	pip3 install virtualenv
	virtualenv -p /usr/local/Cellar/python3/3.6.4_2/bin/python3.6 venv
	source venv/bin/activate

run:
	export FLASK_DEBUG=1
	python hello.py
