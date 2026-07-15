.PHONY: install run test sample docker clean

install:
	pip install -r requirements-dev.txt

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

clean:
	rm -rf data/output/*
	rm -rf logs/*