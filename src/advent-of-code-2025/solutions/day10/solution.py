# puzzle prompt: https://adventofcode.com/2025/day/10

import itertools
import time

import z3

from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 10

    _is_debugging = False

    def Parse(self, machine):
        pattern, *buttons, joltages = machine.split()

        pattern = pattern[1:-1]  # pattern is inside brackets

        buttons = [set(map(int, button[1:-1].split(","))) for button in buttons]

        joltages = map(int, joltages[1:-1].split(","))

        return pattern, *buttons, joltages

    def TurnOnMachines(self, input):
        presses = 0

        # just brute-force which ones to press
        for machine in input:
            pattern, *buttons, _ = self.Parse(machine)

            presses += next(
                N
                for N in itertools.count(0)
                for pressed in itertools.combinations(buttons, N)
                if (
                    "".join(
                        ".#"[sum((i in button for button in pressed)) % 2]
                        for i in range(len(pattern))
                    )
                    == pattern
                )
            )

        return presses

    # we need to solve several equations like Ax = B with the goal to minimize sum(x)
    # using Z3 (day 24, 2023/day 13, 2024)
    def SetJoltage(self, input):
        total = 0

        for machine in input:
            _, *buttons, joltages = self.Parse(machine)

            # variables available to Z3
            presses = [z3.Int(f"press{i}") for i in range(len(buttons))]

            solver = z3.Optimize()

            # constraints
            # button was pressed
            solver.add(z3.And([press >= 0 for press in presses]))
            # sum of the presses must be the joltage
            solver.add(
                z3.And(
                    [
                        sum(
                            presses[j]
                            for j, button in enumerate(buttons)
                            if i in button
                        )
                        == joltage
                        for i, joltage in enumerate(joltages)
                    ]
                )
            )

            # goal
            solver.minimize(sum(presses))

            # solve
            assert solver.check() == z3.sat
            model = solver.model()
            for press in presses:
                total += model[press].as_long()

        return total

    def pt1(self, input):
        self.debug(input)

        res = self.TurnOnMachines(input)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.SetJoltage(input)

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
