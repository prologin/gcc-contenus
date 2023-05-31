#!/usr/bin/env bash

set -xeuo pipefail

pushd themes/gcc

./build.sh
./compile_resources.sh

popd
