# puzzle prompt: https://adventofcode.com/2025/day/11

import functools
import time
import networkx as nx

from ..base.advent import *

graph = nx.DiGraph()

class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 11

    _is_debugging = False

    def Parse(self, input):        
        graph.clear() #since graph is global, i need to make sure i start clean

        for line in input:
            device, outputs = line.split(": ")
            nodes = [output.strip() for output in outputs.split(" ")]

            for node in nodes:
                graph.add_edge(device, node)

        graph.add_node("out")

    # using kind of hack for part 1 with the parameters, in part 1 I dont care if I visited fft and dac
    # so i pass True so test for part 1 is only if i reached to the end
    #
    # If i make FindPaths a class method (takes self as the first parameter),
    # each instance of Solution gets cached separately.
    # Moreover, the cache will hold references to self,
    # preventing garbage collection and causing state to leak between tests
    # so the static method (which lead me to put graph as global)
    @staticmethod
    @functools.cache
    def FindPaths(curr, end, has_visited_dac, has_visited_fft):
        if curr == "fft":  # magic text from puzzle
            has_visited_dac = True

        if curr == "dac":  # magic text from puzzle
            has_visited_fft = True

        if curr == end:
            return has_visited_dac and has_visited_fft

        # Get successors (neighbors) from the graph
        return sum(
            Solution.FindPaths(node, end, has_visited_dac, has_visited_fft)
            for node in graph.successors(curr)
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
