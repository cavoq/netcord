NAME=netcord
PYTHON=python3.11
PIP=pip3.11
HOST=0.0.0.0
PORT=5000
MAIN=netcord
VERSION=1.1.0


help: ## Get help for Makefile
	@echo "\n#### $(NAME) v$(VERSION) ####\n"
	@echo "Available targets:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo "\n"

install: ## Install requirements locally
	sudo apt-get update && sudo apt-get install -y apt-utils firefox iputils-ping traceroute dnsutils net-tools
	$(PIP) install -r requirements.txt

install-dev: ## Install requirements for development
	$(PIP) install -r requirements-dev.txt

lint: ## Run linter
	$(PYTHON) -m pylint $(MAIN)

test: ## Run tests
	$(PYTHON) -m pytest test/

docker-build: ## Build docker image
	docker build -t $(NAME) .

docker-run: ## Run discord bot inside docker container
	docker run --privileged --network=host --env-file .env --name netcord $(NAME)

docker-sh: ## Shell into docker container
	docker run --network=host --privileged -it $(NAME) sh

docker-remove: ## Remove docker container
	docker container rm $(NAME)

run: ## Run discord bot locally
	$(PYTHON) $(MAIN).py

.PHONY: help docker-build docker-run docker-sh docker-remove run install install-dev lint test
