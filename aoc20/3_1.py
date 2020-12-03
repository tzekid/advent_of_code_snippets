import math

iA = """..##.......
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

iA = open('input_3.txt').read().strip().split('\n')

slope_x = 3
slope_y = 1
min_forest_width = slope_x * len(iA)
forest_width = len(iA[0])
forest_width_multipl = math.ceil(min_forest_width / forest_width)

# TODO why is last line empty?
iA = [row * forest_width_multipl for row in iA][:-1]

trees_count = 0
coord_y, coord_x = slope_y, slope_x
for y in range(len(iA) - 1):
    tile = iA[coord_y][coord_x]
    if tile == "#":
        trees_count += 1
    coord_y += slope_y
    coord_x += slope_x
print(trees_count)