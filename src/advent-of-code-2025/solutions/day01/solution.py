# puzzle prompt: https://adventofcode.com/2025/day/1

import sys
import time

sys.path.insert(0, "..")

from base.advent import *  # type: ignore


class Solution(InputAsLinesSolution):  # type: ignore
    _year = 2025
    _day = 1

    _is_debugging = False

    def parse(self, instruction):
        direction = -1 if instruction[0] == "L" else 1
        clicks = int(instruction[1:])
        return direction, clicks

    def turn(self, input):
        instructions = [self.parse(instruction) for instruction in input]

        dial = 50  # magic number given by the puzzle

        hits, passes = 0, 0

        for direction, clicks in instructions:
            offset_to_zero = dial or 100 if direction < 0 else 100 - dial

            # Rotate the dial
            dial = (dial + direction * clicks) % 100

            # dial must be exactly 0
            if dial == 0:
                hits += 1

            if clicks >= offset_to_zero:
                passes += (clicks - offset_to_zero) // 100 + 1

        return hits, passes

    def pt1(self, input):
        self.debug(input)

        res = self.turn(input)

        return res[0]

    def pt2(self, input):
        self.debug(input)

        res = self.turn(input)

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
