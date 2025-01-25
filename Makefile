dev-install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

fmt:
	isort .
	black .

lint:
	flake8 .
	mypy .

tag:
	make lint
	make test
	git for-each-ref --sort=-creatordate --format '%(refname:short)' refs/tags | head -n 1
	@read -p "Enter tag name: " tag_name; \
	git tag -a "$$tag_name" -m "$$tag_name" && git push origin "$$tag_name"

run:
	python scr/main.py

test:
	pytest --cov=src src/tests --blockage

