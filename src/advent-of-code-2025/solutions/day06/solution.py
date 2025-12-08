# puzzle prompt: https://adventofcode.com/2025/day/6

import operator
import re
import time
from functools import reduce

from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 6

    _is_debugging = False

    def Parse(self, input):
        numbers = []

        # this works for part 1 but for part 2 i cannot strip the spaces
        # numbers = [list(col) for col in zip(*[re.findall(r"\d+", row) for row in input[:-1]])]
        #
        # notice the space in the pattern
        matches = list(re.finditer(r"(\W) +", input[-1] + " "))

        for match in matches:
            begin = match.start()
            end = begin + len(match.group(0)) - 1

            parts = [row[begin:end] for row in input[:-1]]
            numbers.append(parts)

        ops = re.findall(r"[+*]", input[-1])

        return numbers, ops

    def Calculate(self, line, op):
        numbers = map(int, line)

        if op == "+":
            return reduce(operator.add, numbers, 0)
        else:
            return reduce(operator.mul, numbers, 1)

    def DoHomework(self, input):
        numbers, ops = self.Parse(input)
        horz = 0
        vert = 0

        for i in range(len(ops)):
            # Part 1: horizontal calculation
            horz += self.Calculate(numbers[i], ops[i])

            # Part 2: vertical calculation
            length = len(numbers[i][0])

            parts = [
                "".join(numbers[i][row][n] for row in range(len(numbers[i])))
                for n in range(length)
            ]
            vert += self.Calculate(parts, ops[i])

        return horz, vert

    def pt1(self, input):
        self.debug(input)

        res = self.DoHomework(input)

        return res[0]

    def pt2(self, input):
        self.debug(input)

        res = self.DoHomework(input)

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
