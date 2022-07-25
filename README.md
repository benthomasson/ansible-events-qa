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
