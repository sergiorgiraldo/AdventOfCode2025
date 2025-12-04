# puzzle prompt: https://adventofcode.com/2025/day/2

import time

from ..base.advent import *


class Solution(InputAsStringSolution):
    _year = 2025
    _day = 2

    _is_debugging = False

    def checkIds(self, input):
        invalids_single_rep = 0
        invalids_multiple_rep = 0

        # i wanted to use ranges as variable name but range is a keyword :)
        intervals = [interval for interval in input.split(",")]

        for interval in intervals:
            min, max = map(int, interval.split("-"))

            for id in range(min, max + 1):
                id_as_string = str(id)
                length = len(id_as_string)
                invalid_ids = set()

                for offset in range(2, length + 1):
                    # make sure we can divide the string in equal pieces
                    # e.g if len is 10, i can make sections of 1, 2, 5 characters
                    if length % offset == 0:
                        size = length // offset
                        sections = [
                            id_as_string[i * size : (i + 1) * size]
                            for i in range(offset)
                        ]

                        # in part 1, simply calculate middle of the id and see if they match, like 4545
                        # i build (4,5,4,5)/(45,45)
                        if len(sections) == 2 and sections[0] == sections[1]:
                            invalids_single_rep += id

                        # in part 2, there can be repetition in more substrings, like 454545
                        # i build (4,5,4,5,4,5) / (45,45,45) / (454,545)
                        if all(section == sections[0] for section in sections):
                            invalid_ids.add(id)

                invalids_multiple_rep += sum(invalid_ids)

        return invalids_single_rep, invalids_multiple_rep

    def pt1(self, input):
        self.debug(input)

        res = self.checkIds(input)

        return res[0]

    def pt2(self, input):
        self.debug(input)

        res = self.checkIds(input)

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
