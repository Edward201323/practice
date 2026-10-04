class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1: island
        2: water

        dfs(row, col):
            if the row is out of bounds:
                return
            if the col is out of bounds:
                return
            if the current cell is not equal to one
                return

            set the current cell equal to zero

            run dfs on all of the neighbors

        itterate through the grid:
            if curr == "1":
                dfs the entire island: to set every single piece of the island as one
                
        """

        rows, cols = len(grid), len(grid[0])
        sol = 0

        def dfs(row, col):
            if row < 0 or row >= rows:
                return
            if col < 0 or col >= cols:
                return
            if grid[row][col] != "0":
                return
            
            grid[row][col] = "0"

            dfs(row, col)
            dfs(row, col)
            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    sol += 1

        return sol
        
        





