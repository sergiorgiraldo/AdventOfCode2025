import unittest

from ..day01.solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        input = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        self.assertEqual(solution.pt1(input), 3, "Oops")

    def test_part2(self):
        input = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        self.assertEqual(solution.pt2(input), 6, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
