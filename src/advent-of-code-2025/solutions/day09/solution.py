# puzzle prompt: https://adventofcode.com/2025/day/9

import time

from ..base.advent import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def GetArea(self, other):
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)

class Edge:
    def __init__(self, p1, p2):
        self.horizontal = (p1.y == p2.y)

        smaller = (p1.x < p2.x) if self.horizontal else (p1.y < p2.y)
        self.p1, self.p2 = (p1, p2) if smaller else (p2, p1)

    # Two edges intersect if:
    # - one is horizontal and the other vertical
    # - the X coordinate of the vertical edge is between the X coordinates of the horizontal edge, and
    # - the Y coordinate of the horizontal edge is between the Y coordinates of the vertical edge.
    #               v vert (AB)
    #    y      - - A - - - -       
    #    y      - - | - - - - 
    #    y      - C ------D -  < horz (CD)
    #    y      - - | - - - -  
    #    y      - - B - - - -   
    #           x x x x x x x
    def Intersects(self, other):
        if self.horizontal == other.horizontal:
            return False

        horizontal = self if self.horizontal else other
        vertical = other if self.horizontal else self

        return (
            vertical.p1.x > horizontal.p1.x and 
            vertical.p1.x < horizontal.p2.x and 
            horizontal.p1.y > vertical.p1.y and 
            horizontal.p1.y < vertical.p2.y
        )


class Polygon:
    def __init__(self, points):
        self.points = points
        self.edges = []

        for i, point in enumerate(points):
            next_point = points[(i + 1) % len(points)]
            self.edges.append(Edge(point, next_point))

    def Intersects(self, other_edge):
        return any(polygon_edge.Intersects(other_edge) for polygon_edge in self.edges)

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
        red_and_any = -1
        red_and_green = -1

        # Iterate all pairs of points
        for i in range(grid_size):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                # Compute area, then update best answer for part 1 if it's larger
                area = p1.GetArea(p2)
                red_and_any = max(red_and_any, area)

                # For part 2 we build four edges that represent the rectangle being checked, then check to see if any edge
                # intersect our polygon's edges. If no intersections, it is a good rectangle.
                # example, from the puzzle unit test
                # 0            13
                # .............. 0
                # .......#XXX#.. 1
                # .......XXXXX.. 2
                # ..#XXXX#XXXX.. 3
                # ..XXXXXXXXXX.. 4
                # ..#XXXXXX#XX.. 5
                # .........XXX.. 6
                # .........#X#.. 7
                # .............. 8               
                # solution will be from rows 3/5
                # but get reds (11,1) and (2,5), it will be a bigger rectangle. But red (7,1) will intercept, in other 
                # words, there are tiles not red/green
                # but .... edges that share a vertex are considered to intersect,
                # which is guaranteed to happen since all the rectangle's vertices are also vertices of the polygon.
                # hack: shrink the rectangle for intersection testing

                x1 = min(p1.x, p2.x) + 0.5
                x2 = max(p1.x, p2.x) - 0.5
                y1 = min(p1.y, p2.y) + 0.5
                y2 = max(p1.y, p2.y) - 0.5

                rectangle = Polygon([Point(x1, y1), Point(x2, y1), Point(x2, y2), Point(x1, y2)])

                # Rectangle is fully inside polygon; update best answer for part 2 if it's larger
                if all(not polygon.Intersects(edge) for edge in rectangle.edges):
                    red_and_green = max(red_and_green, area)

        return [red_and_any, red_and_green]

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
