# puzzle prompt: https://adventofcode.com/2025/day/3

import time

from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 3

    _is_debugging = False

    def turnOnBatteries(self, input, howmany):
        total = []

        for bank in input:
            length = len(bank)
            joltages = [int(joltage) for joltage in bank]
            slots_available = howmany
            on = []

            offset = -1
            # doing slices in the bank, ensuring there are enough batteries left
            #
            # bank is 987654321111111 and i need 2 batteries
            # i can make slices of 14, so my slices will be
            # [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1],[8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]
            #
            # bank is 987654321111111 and i need 12 batteries
            # i can make slices of 4 (pick 1 and leave 11 batteries), so my slices will be
            # [9, 8, 7, 6],[8, 7, 6, 5],[7, 6, 5, 4],...
            #
            # after picking a battery, I discard the batteries before it, they cannot be rearranged
            while slots_available:
                subset = joltages[offset + 1 : length - slots_available + 1]
                max_joltage = max(subset)

                # recalculate the position where to start next subset
                offset = joltages.index(max_joltage, offset + 1)

                on.append(max_joltage)

                slots_available -= 1

            # this is first_digit * 10^position + second_digit * 10^position, etc
            # [3,4] => 3*10^1 + 4*10^0
            total.append(
                sum(digit * 10 ** (len(on) - i - 1) for i, digit in enumerate(on))
            )

        return sum(total)

    def pt1(self, input):
        self.debug(input)

        res = self.turnOnBatteries(input, 2)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.turnOnBatteries(input, 12)

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
