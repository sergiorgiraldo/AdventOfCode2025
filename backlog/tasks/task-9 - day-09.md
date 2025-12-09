---
id: task-9
title: day 09
status: Done
assignee: []
created_date: '2025-11-19 09:52'
labels: []
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Lets help the elvs with the decoration, doing a big red/green tiles grid
<!-- SECTION:DESCRIPTION:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
part 1 is easy, just calculate the largest area for each pair. 

For the PART 2, a rectangle should only be counted if it lies entirely within the boundary created by the input points. To determine if one polygon (A) is fully enclosed by another polygon (B), we need to verify two conditions: at least one corner point of A must be located within B's interior, and A's sides cannot cross any of B's sides.

Luckily, verifying corner positions isn't necessary in our case. This is because each corner of the rectangle we're examining already exists as a corner point of the polygon itself, meaning it's automatically considered to be inside. Therefore, we only need to verify that no sides intersect.
<!-- SECTION:NOTES:END -->