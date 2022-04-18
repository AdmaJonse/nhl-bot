.PHONY: test
test:
	python -m unittest

.PHONY: build
build:
	docker build . -t avalanchebot
	docker tag avalanchebot avalanchebot.azurecr.io/avalanchebot:latest

.PHONY: deploy
deploy: build
	docker push avalanchebot.azurecr.io/avalanchebot:latest