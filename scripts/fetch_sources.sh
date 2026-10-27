#!/usr/bin/env bash
set -euo pipefail

mkdir -p raw/indus

if [ ! -d raw/indus/indus-website ]; then
  git clone --depth 1 https://github.com/yajnadevam/indus-website.git raw/indus/indus-website
else
  echo "skip: raw/indus/indus-website already exists"
fi

if [ ! -d raw/indus/cisi-mayig ]; then
  git clone --depth 1 https://github.com/mayig/indus-valley-script-corpus.git raw/indus/cisi-mayig
else
  echo "skip: raw/indus/cisi-mayig already exists"
fi

echo "indus-website: $(git -C raw/indus/indus-website rev-parse HEAD)"
echo "cisi-mayig: $(git -C raw/indus/cisi-mayig rev-parse HEAD)"
