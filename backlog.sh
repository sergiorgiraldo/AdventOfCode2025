#!/bin/sh

cp ./backlog/Backlog.Final.md ./viewer/Backlog.md

for day in $(seq -w 01 12); do
    cp "./backlog/tasks/task-${day#0} - day-$day.md" ./viewer/
done