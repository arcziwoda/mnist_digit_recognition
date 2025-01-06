.PHONY: run clean install

PYTHON_VERSION = 3.11.10

install:
	poetry env use $(PYTHON_VERSION)
	poetry install

clean:
	poetry env remove --all

