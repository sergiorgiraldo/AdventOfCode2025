import unittest

from ..day12.solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = ["0:",
                "###",
                "##.",
                "##.",
                "",
                "1:",
                "###",
                "##.",
                ".##",
                "",
                "2:",
                ".##",
                "###",
                "##.",
                "",
                "3:",
                "##.",
                "###",
                "##.",
                "",
                "4:",
                "###",
                "#..",
                "###",
                "",
                "5:",
                "###",
                ".#.",
                "###",
                "",
                "4x4: 0 0 0 0 2 0",
                "12x5: 1 0 1 0 2 2",
                "12x5: 1 0 1 0 3 2"]
        self.assertEqual(solution.pt1(input), 2, "Oops")

    # def test_part2(self):
    # input = ""
    # self.assertEqual(solution.pt2(input), "", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
