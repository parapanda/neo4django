#!/usr/bin/env bash

COMMAND=$(basename "${0}")
BASE_DIR=$(readlink -f $(dirname "${0}"))

if [ $# -gt 0 ]; then
    echo 'Error: invalid parameters specified' >&2
    echo '' >&2
    echo "Usage:\n    ${COMMAND}"  >&2
    exit 1
fi

cd "${BASE_DIR}" && docker-compose kill ; docker-compose rm -f
