#!/usr/bin/env bash

set -xeuo pipefail


pushd content/divers/projet_jeu
tar czvf resources.tar.gz resources/sprites
popd

pushd themes/gcc
./build.sh
popd
