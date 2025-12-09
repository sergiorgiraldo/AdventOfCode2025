import unittest

from ..day09.solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = ["7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3"]
        self.assertEqual(solution.pt1(input), 50, "Oops")

    def test_part2(self):
        input = ["7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3"]
        self.assertEqual(solution.pt2(input), 24, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
