PYTHON = python3
APPDIR = bump
TESTDIR = tests

check:
	$(PYTHON) -m pep8 $(APPDIR)
	$(PYTHON) -m pyflakes $(APPDIR)

lint: check
	$(PYTHON) -m pylint $(APPDIR)

init:
	FLASK_APP=$(APPDIR)/setup.py flask initdb

run:
	$(PYTHON) run.py 

test:
	$(PYTHON) -m $(APPDIR)/$(TESTDIR)
