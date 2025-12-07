# puzzle prompt: https://adventofcode.com/2025/day/4

import time

from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 4

    _is_debugging = False

    #         col
    #       @  @  @
    #  row  @  |  @
    #       @  @  @
    #
    # Scan the @ positions, there must be less than 4 around the Roll |
    def InspectRoll(self, input, row, col):
        if input[row][col] != "@":
            return False

        row_bgn = max(0, row - 1)
        row_end = min(row + 1, len(input) - 1)
        col_bgn = max(0, col - 1)
        col_end = min(col + 1, len(input[row]) - 1)

        rolls = sum(
            input[row_adj][col_adj] == "@"
            for row_adj in range(row_bgn, row_end + 1)
            for col_adj in range(col_bgn, col_end + 1)
        )

        return rolls < 5  # magic number given by the puzzle

    def DetermineRolls(self, input):
        res = sum(
            1
            for row in range(len(input))
            for col in range(len(input[row]))
            if self.InspectRoll(input, row, col)
        )

        return res

    # same algorithm as in determine but now you go back and check again if more rolls can be removed
    def RemoveRolls(self, input):
        res = 0

        grid = [list(line) for line in input]  # input may change

        while True:
            lifted = 0

            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if self.InspectRoll(grid, row, col):
                        grid[row][col] = "x"
                        lifted += 1

            if lifted == 0:
                break

            res += lifted

        return res

    def pt1(self, input):
        # self.debug(input)

        res = self.DetermineRolls(input)

        return res

    def pt2(self, input):
        # self.debug(input)

        res = self.RemoveRolls(input)

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
