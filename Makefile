SHELL:=/bin/bash
ARGS = $(filter-out $@,$(MAKECMDGOALS))
MAKEFLAGS += --silent
BASE_PATH=${PWD}
PYTHON_EXEC=python
VENV_PATH=~/venv/cabot-alert-teams

export $(shell sed 's/=.*//' src/.env)
show_env:
	# Show wich DOCKER_COMPOSE_FILE and ENV the recipes will user
	# It should be referenced by all other recipes you want it to show.
	# It's only printed once even when more than a recipe executed uses it
	sh -c "if [ \"${ENV_PRINTED:-0}\" != \"1\" ]; \
	then \
		echo DOCKER_COMPOSE_FILE = \"${DOCKER_COMPOSE_FILE}\"; \
		echo OSFLAG = \"${OSFLAG}\"; \
	fi; \
	ENV_PRINTED=1;"

flake8: show_env
	echo "verify pep8 ..."
	black . && isort . && flake8 .

create_venv: show_env
	sudo apt-get install python3-dev python3-wheel python-dev gcc libpq-dev -y
	python3 -m venv ${VENV_PATH}
	${VENV_PATH}/bin/python -m pip install --upgrade pip setuptools wheel
	${VENV_PATH}/bin/pip install -r ./requirements.txt

upgrade_packages: show_env pip_install
	pip-upgrade --skip-virtualenv-check

test: show_env
	cd cabot_alert_teams && pytest .

test-watch: show_env
	cd cabot_alert_teams && ptw -- --last-failed --new-first

pip_install: show_env
	${PYTHON_EXEC} -m pip install -r requirements.txt