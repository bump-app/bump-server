PYTHON = python3
APPDIR = bump
DB_NAME = bump.db
TESTDIR = test
TESTCASE = test_bump

check:
	$(PYTHON) -m pep8 $(APPDIR)
	$(PYTHON) -m pyflakes $(APPDIR)

lint: check
	$(PYTHON) -m pylint $(APPDIR)

init:
	FLASK_APP=$(APPDIR)/__init__.py flask initdb

run:
	$(PYTHON) run.py 

.PHONY: all test clean
test:
	$(PYTHON) -m unittest $(TESTDIR).$(TESTCASE)

reset-db:
	rm -i $(APPDIR)/$(DB_NAME)
	FLASK_APP=$(APPDIR)/__init__.py flask initdb

