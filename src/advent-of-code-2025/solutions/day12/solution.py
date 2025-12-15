# puzzle prompt: https://adventofcode.com/2025/day/12

import time

from ..base.advent import *
class Solution(InputAsLinesSolution):
    _year = 2025
    _day = 12

    _is_debugging = False

    def Parse(self, input):
        presents = []

        while "" in input:
            offset = input.index("")
            presents.append([present for present in input[1:offset]])
            input = input[offset + 1 :]
        
        regions = input

        return presents, regions

    #only works in puzzle, not in unit test    
    def ArrangePresents_Alternative(self, input):
        presents, regions = self.Parse(input)

        total = 0
                
        for region in regions:
            dimensions, info = region.split(": ")

            x, y = map(int, dimensions.split("x"))
            
            info = list(map(int, info.split(" ")))

            required = sum(amount * sum(row.count("#") 
                            for row in presents[idx]) 
                            for idx, amount in enumerate(info))

            #Failed. Spaces not enough
            if x * y < required:
                continue                
            
            total += 1

        return total
    
    #the unit test only works if you try to change orientations
    #but the puzzle itself works if you just try the total sizes (alternative method below)
    def ArrangePresents(self, input):

        def is_filled(presents, area_map, aux_list):
            shapes = []
            for present in presents:
                curr_shapes = set()
                for _ in range(4):
                    # rotate 90 degrees
                    present = tuple(tuple(s) for s in zip(*present[::-1]))
                    curr_shapes.add(present)
                    # flip horizontally
                    present = tuple(tuple(s[::-1]) for s in present)
                    curr_shapes.add(present)
                shapes.append(curr_shapes)

            sorted_list = sorted([idx for idx, amount in enumerate(aux_list) for _ in range(amount)], key=lambda idx: sum(line.count("#") for line in presents[idx]), reverse=True)

            def try_fill(present_idx, start_pos):
                if present_idx == len(sorted_list):
                    return True

                area_height, area_width = len(area_map), len(area_map[0])
                idx = sorted_list[present_idx]
                for y in range(area_height):
                    for x in range(area_width):
                        if (y, x) < start_pos:
                            continue
                        for shape in shapes[idx]:
                            h, w = len(shape), len(shape[0])
                            if y + h > area_height or x + w > area_width:
                                continue

                            valid = True
                            for dy in range(h):
                                for dx in range(w):
                                    if shape[dy][dx] == "#" and area_map[y + dy][x + dx] == "#":
                                        valid = False
                                        break
                                if not valid:
                                    break

                            if valid:
                                for dy in range(h):
                                    for dx in range(w):
                                        if shape[dy][dx] == "#":
                                            area_map[y + dy][x + dx] = "#"

                                if try_fill(present_idx + 1, (y, x)):
                                    return True

                                # failed, back to previous state
                                for dy in range(h):
                                    for dx in range(w):
                                        if shape[dy][dx] == "#":
                                            area_map[y + dy][x + dx] = "."

                return False

            return try_fill(0, (0, 0))

        presents, regions = self.Parse(input)

        total = 0

        for region in regions:
            dimensions, info = region.split(": ")

            x, y = map(int, dimensions.split("x"))

            info = list(map(int, info.split()))

            required = sum(amount * sum(row.count("#") 
                            for row in presents[idx]) 
                            for idx, amount in enumerate(info))

            area_map = [["." for _ in range(x)] for _ in range(y)]

            #Failed. Spaces not enough
            if x * y < required:
                continue

            total = total + 1 if is_filled(presents, area_map, info) else total        

        return total
    
    def pt1(self, input):
        self.debug(input)
        
        res = self.ArrangePresents(input)
        
        return res

    def pt2(self, input):
        self.debug(input)

        return "Merry Christmas"

    def part_1(self):
        start_time = time.time()

        res = self.pt1(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.pt2(self.input)

        end_time = time.time()

        # self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
