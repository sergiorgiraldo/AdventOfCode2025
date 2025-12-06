import unittest

from ..day06.solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = [
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  ",
        ]
        self.assertEqual(solution.pt1(input), 4277556, "Oops")

    def test_part2(self):
        input = [
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  ",
        ]
        self.assertEqual(solution.pt2(input), 3263827, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
