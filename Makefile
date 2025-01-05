.PHONY: run clean install

ENTRYPOINT = digit-recognition

PYTHON_VERSION = 3.11.10

run:
	poetry run $(ENTRYPOINT)

install:
	poetry env use $(PYTHON_VERSION)
	poetry install

clean:
	poetry env remove --all

