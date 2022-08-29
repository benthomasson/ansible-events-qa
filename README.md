# Ansible Events QA

Black box tests and tools for ansible events QA

## Install dev environment

Requires python 3

- Clone this repository

```sh
git clone git@github.com:Alex-Izquierdo/ansible-events-qa.git
```

- Create a virtualenv and activate it

```sh
python3 -m venv .venv
source .venv/bin/activate
```

- Install

```sh
pip install -U pip hatch
pip install -e '.[dev]'
```

- enable pre-commit (optional)

```sh
pre-commit install
```

## Generate API client

The API client is generated with [openapi-generator project](https://openapi-generator.tech/)

First, you must [install it](https://github.com/OpenAPITools/openapi-generator#1---installation):

```
curl https://raw.githubusercontent.com/OpenAPITools/openapi-generator/master/bin/utils/openapi-generator-cli.sh --output $HOME/.local/bin/openapi-generator
chmod +x $HOME/.local/bin/openapi-generator
```

There is a simple script for generation:

```
./utils/api-client-generator/generate.sh
```
