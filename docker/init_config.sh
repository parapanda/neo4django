#!/usr/bin/env bash

COMMAND=$(basename "${0}")
BASE_DIR=$(readlink -f $(dirname "${0}"))

if [ $# -gt 1 ]; then
    echo 'Error: invalid parameters specified' >&2
    echo '' >&2
    echo "Usage:\n    ${COMMAND} [ neo4j_version ]"  >&2
    exit 1
fi

if [ $# -gt 0 ]; then
    neo4j_version="${1}"; shift
else
    neo4j_version='2.3.2'
fi

docker run --rm --volume="${BASE_DIR}/conf:/conf/" "neo4j:${neo4j_version}" dump-config
