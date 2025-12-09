# puzzle prompt: https://adventofcode.com/2025/day/9

import time

from ..base.advent import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self, other):
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)


class Edge:
    def __init__(self, p1, p2):
        self.horizontal = p1.y == p2.y

        if self.horizontal:
            self.p1 = p1 if p1.x < p2.x else p2
            self.p2 = p2 if p1.x < p2.x else p1
        else:
            self.p1 = p1 if p1.y < p2.y else p2
            self.p2 = p2 if p1.y < p2.y else p1

    # Two edges intersect if:
    #
    # - one is horizontal and the other vertical
    # - the X coordinate of the vertical edge is between the X coordinates of the horizontal edge, and
    # - the Y coordinate of the horizontal edge is between the Y coordinates of the vertical edge.
    #    y            '
    #    y      - - - - - - -
    #    y            '
    #           x x x x x x x
    def intersects(self, other):
        if self.horizontal == other.horizontal:
            return False

        horizontal = self if self.horizontal else other
        vertical = other if self.horizontal else self

        return (
            vertical.p1.x > horizontal.p1.x
            and vertical.p1.x < horizontal.p2.x
            and horizontal.p1.y > vertical.p1.y
            and horizontal.p1.y < vertical.p2.y
        )


class Polygon:
    def __init__(self, points):
        self.points = points
        self.edges = []
        for i, p in enumerate(points):
            next_point = points[(i + 1) % len(points)]
            self.edges.append(Edge(p, next_point))

    def intersects(self, edge):
        return any(e.intersects(edge) for e in self.edges)


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 9

    _is_debugging = False

    def Parse(self, input):
        points = []
        for line in input:
            x, y = map(int, line.split(","))
            points.append(Point(x, y))

        polygon = Polygon(points)

        return points, polygon

    def RetileGrid(self, input):
        points, polygon = self.Parse(input)

        grid_size = len(points) - 1
        red = -1
        red_and_green = -1

        # Iterate all pairs of points
        for i in range(grid_size):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                # Compute area, then update best answer for part 1 if it"s larger
                area = p1.area(p2)
                red = max(red, area)

                # for part 2 we build four edges that represent the rectangle being checked, then check to see if any
                # intersect our polygon's edges. If no intersections, it is a good rectangle.
                # but .... edges that share a vertex are considered to intersect,
                # which is guaranteed to happen since all the rectangle's vertices are also vertices of the polygon.
                # hack: shrink the rectangle for intersection testing
                x1 = min(p1.x, p2.x) + 0.5
                x2 = max(p1.x, p2.x) - 0.5
                y1 = min(p1.y, p2.y) + 0.5
                y2 = max(p1.y, p2.y) - 0.5
                rect = Polygon(
                    [Point(x1, y1), Point(x2, y1), Point(x2, y2), Point(x1, y2)]
                )

                if not any(polygon.intersects(edge) for edge in rect.edges):
                    # Rectangle is fully inside polygon; update best answer for part 2 if it"s larger
                    red_and_green = max(red_and_green, area)

        return [red, red_and_green]

    def pt1(self, input):
        self.debug(input)

        res = self.RetileGrid(input)

        return res[0]

    def pt2(self, input):
        self.debug(input)

        res = self.RetileGrid(input)

        return res[1]

    def part_1(self):
        start_time = time.time()

        res = self.pt1(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.pt2(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
