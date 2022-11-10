#!/usr/bin/env bash

set -xeuo pipefail


pushd content/divers/projet_jeu
tar czvf resources.tar.gz resources/sprites
popd


mkdir -p themes/gcc/static/js/codemirror/mode/
mkdir -p themes/gcc/static/css/codemirror/theme/

cp node_modules/codemirror/lib/codemirror.js themes/gcc/static/js/codemirror/
cp  node_modules/codemirror/mode/python/python.js \
    node_modules/codemirror/mode/xml/xml.js \
    node_modules/codemirror/mode/javascript/javascript.js \
    node_modules/codemirror/mode/css/css.js \
    node_modules/codemirror/mode/htmlmixed/htmlmixed.js \
    themes/gcc/static/js/codemirror/mode/

cp node_modules/codemirror/theme/monokai.css themes/gcc/static/css/codemirror/theme/
cp node_modules/codemirror/lib/codemirror.css themes/gcc/static/css/codemirror/

cp node_modules/jquery/dist/jquery.min.js themes/gcc/static/js/
cp node_modules/skulpt/dist/skulpt.min.js node_modules/skulpt/dist/skulpt-stdlib.js themes/gcc/static/js/
cp node_modules/mathjax/es5/tex-svg.js themes/gcc/static/js/