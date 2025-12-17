# puzzle prompt: https://adventofcode.com/2025/day/4

import time
from collections import defaultdict
from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 4

    _is_debugging = False

    # grids are good as complex numbers (day 10, 2024)
    def Parse(self, input):
        grid = defaultdict(lambda: ".")
        
        for i, line in enumerate(input):
            for j, c in enumerate(line):
                grid[i + 1j * j] = c
        
        return grid, i + 1, j + 1

    #         col
    #       @  @  @
    #  row  @  |  @
    #       @  @  @
    #
    # Scan the @ positions, there must be less than 4 around the Roll |
    def InspectRoll(self, grid, i, j):
        position = i + 1j * j

        if grid[position] != "@":
            return False

        directions = [
            -1-1j,  -1+0j,  -1+1j,
            0-1j,           0+1j, 
            1-1j,   1+0j,   1+1j  
        ]

        rolls = sum(
            1 for direction in directions 
            if grid[position + direction] == "@"
        )

        return rolls < 4  # magic number given by the puzzle

    def DetermineRolls(self, input):
        grid, rows, cols = self.Parse(input)

        res = sum(
            1
            for i in range(rows)
            for j in range(cols)
            if self.InspectRoll(grid, i, j)
        )

        return res

    # same algorithm as in determine but now you go back and check again if more rolls can be removed
    def RemoveRolls(self, input):
        res = 0

        grid, rows, cols = self.Parse(input)

        while True:
            lifted = 0

            for i in range(rows):
                for j in range(cols):
                    if self.InspectRoll(grid, i, j):
                        grid[i + 1j * j] = "x"
                        lifted += 1

            if lifted == 0:
                break

            res += lifted

        return res

    def pt1(self, input):
        self.debug(input)

        res = self.DetermineRolls(input)

        return res

    def pt2(self, input):
        self.debug(input)

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
