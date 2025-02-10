.PHONY: install test run build docker-build docker-run clean

install:
	pip install -r requirements.txt

test:
	pytest tests/

run:
	python appl_project/sync_data.py && \
	python appl_project/run_count.py

build:
	python -m build

docker-build:
	docker build -t appl-project .

docker-run:
	docker run --rm appl-project

clean:
	rm -rf dist build *.egg-info
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
