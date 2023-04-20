#!/usr/bin/env bash

set -xeuo pipefail

pushd themes/gcc
./build.sh
popd
