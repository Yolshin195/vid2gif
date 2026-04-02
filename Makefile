# Переменные
PYTHON = python3
VENV = venv
BIN = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: setup run clean help

help:
	@echo "Использование:"
	@echo "  make setup    - установить окружение и зависимости"
	@echo "  make run      - запустить (по умолчанию)"
	@echo "  make clean    - удалить venv"

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Аргументы для запуска
IN ?= input.mp4
OUT ?= result.gif
N ?= 24
W ?= 480

run:
	@if [ ! -d "$(VENV)" ]; then echo "Сначала: make setup"; exit 1; fi
	$(BIN) vid2gif.py $(IN) -o $(OUT) -n $(N) -w $(W)

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +