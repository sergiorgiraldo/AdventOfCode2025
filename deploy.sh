#!/bin/sh

param=$1

if [ -z "$param" ]; then
    param=$(date +%d)
fi

./build-viewer $param

./ruff.sh

./black.sh

markdownlint-cli2 "*.md" --fix

git bumpmajor

git add --all . 

git commit -S -m 'feat!: day '"$param"' completed.'

git push -u origin HEAD

gh pr create --fill --base main

gh pr merge --merge --auto