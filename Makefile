.PHONY: test
test:
	python -m unittest

.PHONY: lint
lint:
	python -m pylint main.py src/

.PHONY: analyze
analyze:
	python -m mypy --ignore-missing-imports main.py src/

.PHONY: build
build:
	docker build . -t avalanchebot
	docker tag avalanchebot avalanchebot.azurecr.io/avalanchebot:latest

.PHONY: deploy
deploy: build
	docker push avalanchebot.azurecr.io/avalanchebot:latest

.PHONY: run
run: build
	docker run avalanchebot.azurecr.io/avalanchebot:latest

.PHONY: clean
clean:
	rm -rf src/__pycache__
	rm -rf test/__pycache__
	rm data.json
	docker system prune --all --force