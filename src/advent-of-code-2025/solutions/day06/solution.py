# puzzle prompt: https://adventofcode.com/2025/day/6

import re
import time
from functools import reduce

from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 6

    _is_debugging = False

    def parse(self, input):
        numbers = []
        matches = list(re.finditer(r"(\W) +", input[-1] + " "))

        for match in matches:
            start = match.start()
            length = len(match.group(0)) - 1
            segment = [row[start : start + length] for row in input[:-1]]
            numbers.append(segment)

        ops = input[-1].replace(" ", "").replace(" ", "")
        ops = list(ops)

        return numbers, ops

    def doHomework(self, input):
        numbers, ops = self.parse(input)

        def calc(arr, op):
            numbers = [int(digit) for digit in arr]
            if op == "+":
                return sum(numbers)
            else:  # multiplication
                return reduce(lambda acc, curr: acc * curr, numbers, 1)

        ans1 = 0
        ans2 = 0

        for i in range(len(ops)):
            # Part 1: horizontal calculation
            ans1 += calc(numbers[i], ops[i])

            # Part 2: vertical calculation (transpose columns)
            length = len(numbers[i][0])

            parts = [
                "".join(numbers[i][row][n] for row in range(len(numbers[i])))
                for n in range(length)
            ]

            ans2 += calc(parts, ops[i])

        return ans1, ans2

    def pt1(self, input):
        self.debug(input)

        res = self.doHomework(input)

        return res[0]

    def pt2(self, input):
        self.debug(input)

        res = self.doHomework(input)

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
