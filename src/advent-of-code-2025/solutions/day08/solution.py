# puzzle prompt: https://adventofcode.com/2025/day/8

import itertools
import math
import operator
import time
from functools import reduce

import matplotlib.pyplot as plt
import networkx as nx

from ..base.advent import *


class Solution(InputAsCSVSolution):
    _year = 2025
    _day = 8

    _is_debugging = False

    # using networkx from 2024 (days 20, 23)

    def Parse(self, input):
        points = [tuple(map(int, point)) for point in input]

        distances = self.GetDistances(points)

        return points, distances

    def GetDistances(self, points):
        def Euclides(points):
            p1, p2 = points
            return math.dist(p1, p2), p1, p2

        distances = list(map(Euclides, itertools.combinations(points, 2)))
        distances.sort()
        return distances

    def GetLargestCircuits(self, input, howmany):
        _, distances = self.Parse(input)

        graph = nx.Graph()

        for _, p1, p2 in distances[:howmany]:
            graph.add_edge(p1, p2)

        self.debug(graph.edges)

        if self._is_debugging:
            nx.draw(graph, with_labels=True)
            plt.show()

        components = [len(c) for c in nx.connected_components(graph)]
        components.sort(reverse=True)

        res = reduce(operator.mul, components[:3], 1)

        return res

    def BuildOneCircuit(self, input):
        points, distances = self.Parse(input)

        graph = nx.Graph()

        for point in points:
            graph.add_node(point)

        self.debug(graph.nodes)

        for _, p1, p2 in distances:
            graph.add_edge(p1, p2)
            if nx.is_connected(graph):
                break

        self.debug(graph.edges)

        if self._is_debugging:
            nx.draw(graph, with_labels=True)
            plt.show()

        return p1[0] * p2[0]

    def pt1(self, input):
        self.debug(input)

        res = self.GetLargestCircuits(input, 1000)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.BuildOneCircuit(input)

        return res

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
