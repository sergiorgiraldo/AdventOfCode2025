# puzzle prompt: https://adventofcode.com/2025/day/1

import time

from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 1

    _is_debugging = False

    def Parse(self, instruction):
        direction = -1 if instruction[0] == "L" else 1
        steps = int(instruction[1:])
        return direction, steps

    def GetPasswordInSafe(self, input):
        dial = 50  # magic number given by the puzzle
        zeroes, clicks = 0, 0
        instructions = [self.Parse(rotation) for rotation in input]

        for direction, steps in instructions:
            # Calculate distance to zero
            offset_to_zero = (dial or 100) if direction < 0 else (100 - dial)

            # Rotate the dial
            dial = (dial + direction * steps) % 100

            zeroes += steps == offset_to_zero  # exactly zero

            # passing/reaching zero
            # can be several times
            clicks += ((steps - offset_to_zero) // 100 + 1) * (steps >= offset_to_zero)

        return zeroes, clicks

    def pt1(self, input):
        self.debug(input)

        res = self.GetPasswordInSafe(input)

        return res[0]

    def pt2(self, input):
        self.debug(input)

        res = self.GetPasswordInSafe(input)

        return res[1]

    # region execute parts
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


# endregion

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
