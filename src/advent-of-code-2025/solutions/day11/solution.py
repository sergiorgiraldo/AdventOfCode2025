# puzzle prompt: https://adventofcode.com/2025/day/11

import functools
import time

import networkx as nx

from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 11

    _is_debugging = False

    graph = nx.DiGraph()

    def Parse(self, input):
        for line in input:
            device, outputs = line.split(": ")
            nodes = [output.strip() for output in outputs.split(" ")]

            for node in nodes:
                self.graph.add_edge(device, node)

        self.graph.add_node("out")

    # using kind of hack for part 1 with the parameters, in part 1 I dont care if I visited fft and dac
    # so i pass True so test for part 1 is only if i reached to the end
    @functools.cache
    def FindPaths(self, curr, end, has_visited_dac, has_visited_fft):
        if curr == "fft":  # magic text from puzzle
            has_visited_dac = True

        if curr == "dac":  # magic text from puzzle
            has_visited_fft = True

        if curr == end:
            return 1 if has_visited_dac and has_visited_fft else 0

        # Get successors (neighbors) from the graph
        return sum(
            self.FindPaths(node, end, has_visited_dac, has_visited_fft)
            for node in self.graph.successors(curr)
        )

    def pt1(self, input):
        self.debug(input)

        self.Parse(input)

        res = self.FindPaths("you", "out", True, True)

        return res

    def pt2(self, input):
        self.debug(input)

        self.Parse(input)

        res = self.FindPaths("svr", "out", False, False)

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
