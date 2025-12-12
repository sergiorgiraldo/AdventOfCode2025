# puzzle prompt: https://adventofcode.com/2025/day/12

import re
import time

from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 12

    _is_debugging = False

    def ArrangePresents(self, lines):
        sizes = {}
        num = 0
        present = 0
        region = 0
        actual_size = 0
        total = 0

        for line in lines:
            if line == "":
                sizes[num] = present
                present = 0
            elif len(line) == 2:
                num = int(line[0])
            elif "#" in line:
                for c in line:
                    if c == "#":
                        present += 1
            else:
                info = line.split(" ")
                parts = info[0].split("x")
                print(parts)
                region = int(parts[0]) * int(parts[1][:-1])
                for i in range(1, len(info)):
                    actual_size += sizes[i - 1] * int(info[i])
                if actual_size <= region:
                    total += 1
                actual_size = 0

        return total

    def pt1(self, input):
        self.debug(input)

        res = self.ArrangePresents(input)

        return res

    def pt2(self, input):
        self.debug(input)

        return "Merry Christmas"

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
