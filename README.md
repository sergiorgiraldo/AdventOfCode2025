# Advent of Code 2025 Python

My solutions to [Advent of Code 2025](https://adventofcode.com/2025) done in Python

[Viewer](https://sergiorgiraldo.github.io/AdventOfCode2025/viewer/)

## Performance

![](https://img.shields.io/badge/day%20📅-1-blue)

![](https://img.shields.io/badge/stars%20⭐-2-yellow)

---

- Based on @xavdid's Python Advent of Code Project Template

## setup

When advent begins, get the session cookie from the page and update these:

- `./.env`
- aoc_session in gh action secret
- aocd token in `~/.config/aocd/token`

### gh actions

- copy .github folder from prev year and change the year

### git crypt

- `git-crypt init`
- `git-crypt add-gpg-user sergio@giraldo.com.br`
- Make sure the .gitattributes are copied from prev year

### version

set to 0.0.0

### iteration

set to 0000

### changelog.md

clean up the file

### viewer

remove links from `viewer/index.html`

## running a day

`cd` to root folder

use the `run.sh` command (see below)

OR

`cd` to the day

`python -m tests --verbose` && `python -m solution`

to make easier, I have this rule for [`ondir`](https://github.com/alecthomas/ondir)

> .ondirrc

```ondir
enter ~/source/AdventOfCode2025/(.*)
    alias pt="python -m tests --verbose"
    alias pr="python -m solution"

leave ~/source/AdventOfCode2025/(.*)
    unalias pt
    unalias pr
```

## Commands

### start

Scaffold files to start a new Advent of Code solution and download the puzzle input and puzzle test input.

Default current year and current day

#### Usage

> `./start [-h] [--year YEAR] [day]`

### run.sh

Run tests or solution for a given day, default current day and tests

It always runs in the venv

#### Usage

> `./run.sh [day] [t|tests|s|solution]`

### markdownlint-cli2

Lint and format markdown files

### ruff.sh

Lint, options in `pyproject.toml`

### black.sh

Format, options in `pyproject.toml`

### deploy.sh

Lint (using Ruff), format (using Black), create viewer, commit to Github and make PR

Default current day

It should be run in **develop** branch

#### Usage

> `./deploy.sh [day]`

### finish.sh

Run once advent is finished and all solutions done.

It will rerun all tests, download all puzzles, rebuild all viewers, format and lint all files. Then generate a final version.

### build-viewer

Generate HTML for viewing the day's solution

#### Usage

> `./build-viewer [day]`
