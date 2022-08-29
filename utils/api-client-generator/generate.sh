#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_DIR=$SCRIPT_DIR/../../
SPEC_URL=${1:-"http://localhost:8080/openapi.json"}


print_error() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $*" >&2
}

check_dependencies() {
    for prog in openapi-generator jq curl; do
        if ! command -v ${prog} &>/dev/null; then
            print_error "${prog} program could not be found. Please install it"
            exit 1
        fi
    done
}

download() {
    if [[ "$SPEC_URL" =~ ^http.* ]]; then
        echo "downloading the spec file as reference"
        curl -q "${SPEC_URL}" --output ./openapi.tmp &>/dev/null
        jq < ./openapi.tmp > openapi.json && rm -rf ./openapi.tmp
    fi
}

generate() {
    openapi-generator generate \
    -g python \
    -i "${SPEC_URL}" \
    -o "${PROJECT_DIR}" \
    -c "${SCRIPT_DIR}/config.yml" \
    --global-property "apiTests=false,modelTests=false"
}

check_dependencies
# generate
download
