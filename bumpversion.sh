#!/bin/bash

set -e

git bumpmajor

if [ ! -f "VERSION" ]; then
    echo "Error: VERSION file not found"
    exit 1
fi

if [ ! -f "pyproject.toml" ]; then
    echo "Error: pyproject.toml file not found"
    exit 1
fi

VERSION=$(cat VERSION | tr -d '[:space:]')

if [ -z "$VERSION" ]; then
    echo "Error: VERSION file is empty"
    exit 1
fi

echo "Updating version to: $VERSION"

sed -i.bak "s/^version[[:space:]]*=.*/version = \"$VERSION\"/" pyproject.toml

if cmp -s pyproject.toml pyproject.toml.bak; then
    echo "Warning: No version field found in pyproject.toml"
    rm pyproject.toml.bak
    exit 1
else
    rm pyproject.toml.bak
fi