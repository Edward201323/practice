class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        max varaible
        
        dfs(row, col):
            if row is out of bounds:
                return 0
            if col is out of bounds:
                return 0
            if the current cell is != 1:
                return 0
            
            set the current cell == 0, so we don't double count the cell later
            traverse all of the current cells neighbors recursively
            return up + down + left + right + 1

        itterate throughout the entire grid:
            if the current cell is equal to 1:
                preform dfs on the cell's island.
                the dfs algorithm should return the amount of cells in the island
                if the value given is greater than the current max, set it as the new max

        """

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col):
            if row < 0 or row >= rows:
                return 0
            if col < 0 or col >= cols:
                return 0
            if grid[row][col] != 1:
                return 0

            grid[row][col] = 0
            total = 0
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for n_row, n_col in neighbors:
                total += dfs(n_row, n_col)

            return 1 + total

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(max_area, area)
        
        return max_area

        