# puzzle prompt: https://adventofcode.com/2025/day/7

import operator
import time
from collections import defaultdict
from functools import reduce

from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 7

    _is_debugging = False

    # grids are good as complex numbers (day 10, 2024)
    def Parse(self, input):
        manifold = defaultdict(int)

        for i, line in enumerate(input):
            for j, c in enumerate(line):
                manifold[i + 1j * j] = c

        splitters = [z for z, c in manifold.items() if c == "^"]
        hits = defaultdict(int, {splitters[0]: 1})

        return splitters, hits

    # look at this at lines marked with X

    # .......S.......
    # .......|.......
    # ......|^|......X
    # ......|.|......X
    # ......^.^......
    # ...............
    # .....^.^.^.....
    # ...............
    # ....^.^...^....
    # ...............
    # ...^.^...^.^...
    # ...............
    # ..^...^.....^..
    # ...............
    # .^.^.^.^.^...^.
    # ...............

    # .......S.......
    # .......|.......
    # ......|^|......
    # ......|.|......X
    # .....|^|^|.....X
    # ...............
    # .....^.^.^.....
    # ...............
    # ....^.^...^....
    # ...............
    # ...^.^...^.^...
    # ...............
    # ..^...^.....^..
    # ...............
    # .^.^.^.^.^...^.
    # ...............

    # the beam will split only if there is a beam on above it and to its left/right
    # and then each splitter hit turns a universe into one additional universe,
    # so we can find the universes summing all splitter hits.
    # the gotcha is that then we must start the investigation from the end:
    # 1. we get a splitter
    # 2. go all the way down and back up
    # 3. see for each interaction if there is one above and left or right
    # 3.a. remember the imaginary part is the y (left or right)
    def FollowBeam(self, input):
        splitters, hits = self.Parse(input)

        for i, splitter in enumerate(splitters):
            for j in range(i - 1, -1, -1):
                above = splitters[j]

                hits[splitter] += (
                    hits[above] if abs(above.imag - splitter.imag) == 1 else 0
                )

                if above.imag == splitter.imag:  # I navigated all the all way up
                    break

        splitted = reduce(operator.add, (1 for value in hits.values() if value != 0), 0)

        timelines = reduce(operator.add, hits.values(), 0) + 1
        # add the original universe

        return splitted, timelines

    def pt1(self, input):
        self.debug(input)

        res = self.FollowBeam(input)

        return res[0]

    def pt2(self, input):
        self.debug(input)

        res = self.FollowBeam(input)

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
