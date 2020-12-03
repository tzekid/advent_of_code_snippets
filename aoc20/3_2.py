import math
from functools import reduce

iA_orig = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split('\n')


iA_orig = open('input_3.txt').read().strip().split('\n')

# slope_x = 3
# slope_y = 1

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

all_trees_count = []
trees_count = 0

for slope in slopes:
    min_forest_width = slope[0] * len(iA_orig)
    forest_width = len(iA_orig[0])
    forest_width_multipl = math.ceil(min_forest_width / forest_width)

    iA = [row * forest_width_multipl for row in iA_orig]

    coord_y, coord_x = slope[1], slope[0]
    for y in range(len(iA) - 1):
        if coord_y > len(iA):
            continue

        tile = iA[coord_y][coord_x]
        if tile == "#":
            trees_count += 1
        coord_y += slope[1]
        coord_x += slope[0]

    print(trees_count)

    all_trees_count.append(trees_count)
    trees_count = 0

trees_mult_count = reduce(lambda x, y: x*y, all_trees_count)
print(trees_mult_count)