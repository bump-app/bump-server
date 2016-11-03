PYTHON = python3
APPDIR = bump

check:
	$(PYTHON) -m pep8 $(APPDIR)
	$(PYTHON) -m pyflakes $(APPDIR)

lint: check
	$(PYTHON) -m pylint $(APPDIR)

run:
	$(PYTHON) -m $(APPDIR)
