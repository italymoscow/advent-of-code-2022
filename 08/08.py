"""
Solution to the Day 8, Part 1 and 2.

Returns:
    PART 1. How many trees are visible from outside the grid: 1679
    PART 2. The highest scenic score possible for any tree: 536625
"""


import os


def part_1(trees_visible_count):
    """
    Solution to Part 1. Prints the result.
    """
    for i in range(1, grid_width - 1):
        for j in range(1, grid_hight - 1):
            tree_height = grid[i][j]

            # Check trees to the left
            max_left = max(grid[i][0:j])
            if tree_height > max_left:
                trees_visible_count += 1
                continue

            # Check trees to the right
            max_right = max(grid[i][j + 1:])
            if tree_height > max_right:
                trees_visible_count += 1
                continue

            # Check trees above
            max_above = max(grid_reversed[j][0:i])
            if tree_height > max_above:
                trees_visible_count += 1
                continue

            # Check trees below
            max_below = max(grid_reversed[j][i + 1:])
            if tree_height > max_below:
                trees_visible_count += 1
                continue

    print("PART 1. How many trees are visible from outside the grid:",
          trees_visible_count)


def part_2():
    """
    Solution to Part 2. Prints the result.
    """
    tree_scores = []
    for i in range(1, grid_width - 1):
        for j in range(1, grid_hight - 1):
            tree_height = grid[i][j]
            tree_score_data = 1

            # Check trees above
            trees_above = grid_reversed[j][0:i]
            trees_visible_count = 0
            for x in reversed(trees_above):
                trees_visible_count += 1
                if x >= tree_height:
                    break
            tree_score_data *= trees_visible_count

            # Check trees below
            trees_below = grid_reversed[j][i + 1:]
            trees_visible_count = 0
            for x in trees_below:
                trees_visible_count += 1
                if x >= tree_height:
                    break
            tree_score_data *= trees_visible_count

            # Check trees to the left
            trees_left = grid[i][0:j]
            trees_visible_count = 0
            for x in reversed(trees_left):
                trees_visible_count += 1
                if x >= tree_height:
                    break
            tree_score_data *= trees_visible_count

            # Check trees to the right
            trees_right = grid[i][j + 1:]
            trees_visible_count = 0
            for x in trees_right:
                trees_visible_count += 1
                if x >= tree_height:
                    break
            tree_score_data *= trees_visible_count

            tree_scores.append(tree_score_data)
    
    highest_score = max(tree_scores)
    
    print("PART 2. The highest scenic score possible for any tree:",
          highest_score)


cur_path = os.path.dirname(os.path.abspath(__file__))
input_file = open(cur_path + "\\08_input.txt", "r")
input_strings = input_file.readlines()
input_file.close()

grid = []
for input_string in input_strings:
    row_hights = list(input_string.rstrip())
    row_hights = list(map(int, row_hights))
    grid.append(row_hights)
grid_width = len(grid[0])
grid_hight = len(grid)

grid_reversed = []
for j in range(0, grid_hight):
    grid_reversed.append([item[j] for item in grid])

trees_edge_count = 2 * (grid_width - 1) + 2 * (grid_hight - 1)
trees_visible_count = trees_edge_count

if __name__ == "__main__":
    part_1(trees_visible_count)
    part_2()
