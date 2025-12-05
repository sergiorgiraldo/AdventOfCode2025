import unittest

from ..day05.solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = [["3-5", "10-14", "16-20", "12-18"], ["1", "5", "8", "11", "17", "32"]]
        self.assertEqual(solution.pt1(input), 3, "Oops")

    def test_part2(self):
        input = [["3-5", "10-14", "16-20", "12-18"], ["1", "5", "8", "11", "17", "32"]]
        self.assertEqual(solution.pt2(input), 14, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
