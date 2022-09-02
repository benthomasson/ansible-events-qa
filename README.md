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

## Usage

```
pytest
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

## Configuration

Configuration is defined in `ansible_events_qa/conf/settings.yaml` and is managed by [dynaconf library](https://dynaconf.readthedocs.io/).
Supports a `.env` file in the root of the project which can have defined environment variables to override default settings.
You can override it with `AEQE_{keyname}={keyvalue}`
The configuration supports multiple environments, you can define it with the environment variable `AEQE_ENV_{environment}`

### encrypted values

You can create encrypted values that will be automatically decrypted. Before you can encrypt a value you must first specify the fernet password by defining the environment variable `AEQE_FERNET_PASSWORD`. If you do not have the fernet password, please contact a team member to acquire it.

You can then use the encrypted value by specifying it with the following pattern: `key: "!fernat:[encrypted data]"`

The encryption uses `cryptography.fernet` which is an easy and reliable symmetric encryption based on AES cipher.

You can use `aeqe` command to encrypt or decrypt values:

```shell
aeqe --encrypt "password"
# gAAAAABjEPXUFt5Oc-ivGsv6SZ9goAp8X_WIIBRJvzvIm7n8AGn18BL9tsAEGW6P2BUN2GjOXyBG711dEGg2s-qOJVAvjR0m4g==
aeqe --decrypt "gAAAAABjEPXUFt5Oc-ivGsv6SZ9goAp8X_WIIBRJvzvIm7n8AGn18BL9tsAEGW6P2BUN2GjOXyBG711dEGg2s-qOJVAvjR0m4g=="
# password
```
