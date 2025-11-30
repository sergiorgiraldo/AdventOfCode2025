#!/bin/sh

cd src/advent-of-code-2025/solutions

for day in $(ls -d day*); do
    cd $day

    echo ""
    echo $day
    
    python -m tests --verbose
    if [ $? -ne 0 ]; then
        echo "Tests failed. Exiting finish.sh."
        exit 1
    fi
    cd ..
done

echo "###########################"
echo "All tests passed."
echo "###########################"

cd ..

./build-viewer

echo "###########################"
echo "Viewers generated."
echo "###########################"

./get-puzzles

echo "###########################"
echo "Puzzles downloaded."
echo '###########################'

./easter-eggs

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

backlog board export
mv ./Backlog.md ./viewer/Backlog.md


git add --all . 

git commit -S -m 'feat!: AOC 2025 completed.'

git push -u origin HEAD

gh pr create --fill --base main

gh pr merge --merge --auto

echo "###########################"
echo "Final version generated."
echo "###########################"