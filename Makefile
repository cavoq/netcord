NAME=netcord
PYTHON=python3
HOST=0.0.0.0
PORT=5000
MAIN=netcord
VERSION=1.0.0


help: ## Get help for Makefile
	@echo "\n#### $(NAME) v$(VERSION) ####\n"
	@echo "Available targets:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo "\n"

install: ## Install requirements locally
	pip3 install -r requirements.txt

test: ## Run tests
	$(PYTHON) -m pytest test/

docker-build: ## Build docker image
	docker build --no-cache -t $(NAME) .

docker-run: ## Run discord bot inside docker container
	docker run --network=host --env-file .env --name netcord $(NAME)

docker-sh: ## Shell into docker container
	docker run -it $(NAME) sh

docker-remove: ## Remove docker container
	docker container rm $(NAME)

run: ## Run discord bot locally
	$(PYTHON) $(MAIN).py

.PHONY: help docker-build docker-run docker-sh docker-remove run install test
