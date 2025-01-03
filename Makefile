.PHONY: run clean install

VENV_DIR = .venv

ENTRYPOINT = number_recognition/app.py

run: $(VENV_DIR)/bin/activate
	$(VENV_DIR)/bin/python $(ENTRYPOINT)

install: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate: requirements.txt
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV_DIR)

