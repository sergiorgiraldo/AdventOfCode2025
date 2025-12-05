# puzzle prompt: https://adventofcode.com/2025/day/5

import time

from ..base.advent import *


class Solution(InputAsBlockSolution):
    _year = 2025
    _day = 5

    _is_debugging = False

    def parse(self, input):
        self.ranges = []
        self.ingredients = []

        for line in input[0]:
            start, end = map(int, line.split("-"))
            self.ranges.append([start, end + 1])

        self.ranges = sorted(self.ranges)

        self.ingredients = list(map(int, input[1]))

    def getGoodIngredients(self, input):
        self.parse(input)

        goods = 0

        goods = sum(
            1
            for id in self.ingredients
            if any(range[0] <= id < range[1] for range in self.ranges)
        )

        return goods

    def getAllIngredients(self, input):
        self.parse(input)

        total = 0
        idx = 0

        while idx < len(self.ranges):
            start, end = self.ranges[idx][0], self.ranges[idx][1]
            idx += 1

            # i stay in this inner loop until my min is not changed
            # my ranges are sorted so my first one is the min, i only have to go checking for the maxes
            # like
            # *******
            #    ******
            #       ******
            # i break when
            # *******
            #          ********
            #
            while (idx < len(self.ranges)) and (self.ranges[idx][0] <= end):
                end = self.ranges[idx][1] if self.ranges[idx][1] > end else end
                idx += 1

            total += end - start

        return total

    def pt1(self, input):
        self.debug(input)

        res = self.getGoodIngredients(input)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.getAllIngredients(input)

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
