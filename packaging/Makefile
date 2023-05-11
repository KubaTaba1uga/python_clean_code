venv_name := .venv
sources := app tests
ignored_err := E501,W503,F405

help:
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with pytest"
	@echo "install - create venv and install requirements.txt"
	@echo "install-dev - create venv and install test-requirements.txt"
	@echo "clean - remove venv"	
	@echo "clean-pyc - remove Python file artifacts"
  @echo "clean-git - remove ignored and not ignored files"

lint:
	flake8 --ignore $(ignored_err) $(sources)
	mypy $(sources)

test:
	pytest -vv

install: 
	pip3 install virtualenv
	python3 -m virtualenv $(venv_name)
	$(venv_name)/bin/python setup.py install

install-dev: 
	pip3 install virtualenv
	python3 -m virtualenv $(venv_name)
	$(venv_name)/bin/python -m pip install -r test-requirements.txt

clean: rm -rf $(venv_name)

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
  
clean-git:
  git clean -fxd
