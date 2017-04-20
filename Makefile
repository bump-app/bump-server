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

init-db:
	$(PYTHON) cli.py initdb

reset-db:
	$(PYTHON) cli.py resetdb

seed:
	$(PYTHON) cli.py seed

run:
	$(PYTHON) cli.py run

.PHONY: all test clean
test:
	$(PYTHON) -m unittest $(TESTDIR).$(TESTCASE)

