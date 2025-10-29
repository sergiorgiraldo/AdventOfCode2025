# Advent of Code 2025 Python

My solutions to [Advent of Code 2025](https://adventofcode.com/2025) done in Python

[Viewer](https://sergiorgiraldo.github.io/AdventOfCode2025/viewer/)

## Performance

![](https://img.shields.io/badge/day%20📅-25-blue)

![](https://img.shields.io/badge/stars%20⭐-50-yellow)

---

- Based on @xavdid's Python Advent of Code Project Template

## setup

When advent begins, get the session cookie from the page and update these:

- `./.env`
- aoc_session in gh action secret
- aocd token in `~/.config/aocd/token`

## gh actions

- copy .github folder from prev year and change the year

## git crypt

- `git-crypt init`
- `git-crypt add-gpg-user sergio@giraldo.com.br`
- Make sure the .gitattributes are copied from prev year

## running a day

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

### markdownlint-cli2

Lint and format markdown files

### `./ruff.sh`

Lint, options in `pyproject.toml`

### `./black.sh`

Format, options in `pyproject.toml`

### `./deploy.sh`

Lint (using Ruff), format (using Black), create viewer, commit to Github and make PR

#### Usage

> `./deploy.sh [day]` # *default current day*
> run in **develop** branch
>

### `./start`

Scaffold files to start a new Advent of Code solution and download the puzzle input and puzzle test input

#### Usage

> `./start [-h] [--year YEAR] [day]` # *default current year and current day*

### `./build-viewer`

Generate HTML for viewing the day's solution

#### Usage

> `./build-viewer {day}`
