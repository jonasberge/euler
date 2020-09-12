VENV=venv


$(VENV):
	python -m venv $(VENV)

upgrade:
	pip install --upgrade pip
	pip install -r requirements.txt


.PHONY: upgrade
