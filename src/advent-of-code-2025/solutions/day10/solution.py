# puzzle prompt: https://adventofcode.com/2025/day/10

import itertools
import time
from functools import reduce
import operator
import z3

from ..base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 10

    _is_debugging = False

    def Parse(self, machine):
        pattern, *wirings, joltages = machine.split()

        pattern = pattern[1:-1]  # pattern is inside brackets

        wirings = [set(map(int, button[1:-1].split(","))) for button in wirings]

        joltages = map(int, joltages[1:-1].split(","))

        return pattern, *wirings, joltages

    def TurnOnMachines(self, input):
        presses = 0

        # just brute-force which ones to press
        for machine in input:
            pattern, *wirings, _ = self.Parse(machine)

            found = False
            for size in itertools.count(0):
                #make combinations of the wirings
                for pressed in itertools.combinations(wirings, size):
                    # Build the result pattern
                    result = ""
                    for i in range(len(pattern)):
                        #how many of the wiring buttons are the position i.
                        count = sum(1 for button in pressed if i in button)
                        #determine if the position should be off (0 = even presses cancel out) or on (1 = odd presses)
                        result += ".#"[count % 2]
                    
                    # Check if it matches
                    if result == pattern:
                        presses += size
                        found = True
                        break
                
                if found:
                    break
                
        return presses

    # we need to solve several equations like Wiring * x = Joltage with the goal to minimize sum(x)
    # using Z3 (day 24, 2023/day 13, 2024)
    def SetJoltage(self, input):
        total = 0

        for machine in input:
            _, *wirings, joltages = self.Parse(machine)

            # variables available to Z3
            # number of wiring schemas
            schemas = [z3.Int(i) for i in range(len(wirings))]

            solver = z3.Optimize()

            # constraints
            
            # buttons of a wiring were pressed
            solver.add(z3.And([presses >= 0 for presses in schemas]))

            # sum of the presses must be the joltage
            solver.add(
                z3.And([
                        sum(schemas[j]
                            for j, buttons in enumerate(wirings)
                            if i in buttons)
                        == joltage
                        for i, joltage in enumerate(joltages)
                    ])
            )

            # goal
            solver.minimize(sum(schemas))

            # solve
            _ = solver.check() #assuming result z3.sat
            model = solver.model()

            total += sum(model[schema].as_long() for schema in schemas)

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
