#!/bin/sh

cd src/advent-of-code-2025/

for day in $(seq -w 01 12); do
    echo ""
    echo $day
    
    python -m solutions.day${day}.tests --verbose

    if [ $? -ne 0 ]; then
        echo "Tests failed. Exiting finish.sh."
        exit 1
    fi
done

cd ../../

echo "###########################"
echo "All tests passed."
echo "###########################"

./build-viewer

echo "###########################"
echo "Viewers generated."
echo "###########################"

./get-puzzles

echo "###########################"
echo "Puzzles downloaded."
echo '###########################'

./get-easter-eggs

echo "###########################"
echo "Easter eggs retrieved."
echo '###########################'

./ruff.sh

./black.sh

markdownlint-cli2 "*.md" --fix

echo "###########################"
echo "Formatted, linked and checked."
echo "###########################"

./bumpversion.sh

echo "###########################"
echo "Backlog"
echo "###########################"

./backlog.sh

git add --all . 

git commit -S -m 'feat!: AOC 2025 completed.'

git push -u origin HEAD

gh pr create --fill --base main

gh pr merge --merge --auto

echo "###########################"
echo "Final version generated."
echo "###########################"