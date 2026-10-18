#!/bin/sh
# Compila con el formato XeLaTeX que incluye patrones de silabeo español
cd "$(dirname "$0")"
for i in 1 2; do xelatex -fmt=fmt/xelatex-es -interaction=nonstopmode "$1" > /dev/null; done
grep -E "^!" "${1%.tex}.log"; grep -c Overfull "${1%.tex}.log"
