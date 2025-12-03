import unittest

from ..day03.solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]
        self.assertEqual(solution.pt1(input), 357, "Oops")

    def test_part2(self):
        input = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]
        self.assertEqual(solution.pt2(input), 3121910778619, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
