PYTHON = python3
APPDIR = bump
TESTDIR = test
TESTCASE = test_bump

check:
	$(PYTHON) -m pep8 $(APPDIR)
	$(PYTHON) -m pyflakes $(APPDIR)

lint: check
	$(PYTHON) -m pylint $(APPDIR)

init:
	FLASK_APP=$(APPDIR)/setup.py flask initdb

run:
	$(PYTHON) run.py 

.PHONY: all test clean
test:
	$(PYTHON) -m unittest $(TESTDIR).$(TESTCASE)
