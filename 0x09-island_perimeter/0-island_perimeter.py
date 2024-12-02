#!/usr/bin/python3
"""
Island Perimeter Calculation Module

This module provides a function to calculate the perimeter of an island
represented in a 2D grid, where land cells are marked with 1 and water
cells with 0.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    Approach: Traverse the grid and count boundary edges for each land cell.

    Args:
        grid (List[List[int]]): A 2D grid representing the island.
                                0 represents water, 1 represents land.

    Returns:
        int: Total perimeter of the island.
    """
    # Early return if grid is empty
    if not grid or not grid[0]:
        return 0

    # Initialize perimeter counter
    perimeter = 0

    # Grid dimensions
    rows, cols = len(grid), len(grid[0])

    # Directions for neighboring cells (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Traverse through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if current cell is land
            if grid[row][col] == 1:
                # Check each neighboring cell
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy

                    # Add perimeter edge if:
                    # 1. Neighboring cell is out of grid bounds (water)
                    # 2. Neighboring cell is water
                    if (new_row < 0 or new_row >= rows or
                            new_col < 0 or new_col >= cols or
                            grid[new_row][new_col] == 0):
                        perimeter += 1

    return perimeter
