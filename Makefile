.PHONY: install run test sample docker

install:
	pip install -r requirements.txt

sample:
	python -m src.generate_sample_data

run:
	python -m src.main \
		--input data/input/sales.xlsx \
		--output data/output/report.xlsx

test:
	pytest

docker:
	docker compose up --build