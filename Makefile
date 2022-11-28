container_registry := 124596083913.dkr.ecr.ca-central-1.amazonaws.com
image_name         := avalanche-bot
image_tag          := latest

.PHONY: test
test:
	python -m pytest --junitxml results.xml test/

.PHONY: lint
lint:
	python -m pylint main.py src/

.PHONY: analyze
analyze:
	python -m mypy --ignore-missing-imports main.py src/

.PHONY: build
build:
	docker build . -t $(image_name)
	docker tag $(image_name) $(container_registry)/$(image_name):$(image_tag)

.PHONY: deploy
deploy: build
	docker push $(container_registry)/$(image_name):$(image_tag)

.PHONY: run
run: build
	docker run $(container_registry)/$(image_name):$(image_tag)

.PHONY: clean
clean:
	rm -rf src/__pycache__
	rm -rf src/events/__pycache__
	rm -rf test/__pycache__
	rm -rf test/test_data/__pycache__
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -f data.json
	rm -f results.xml
