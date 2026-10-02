class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Plan:
        Itterate throughout the graph
            If I come across a unvisited 1, run BFS/DFS on the island to get the area
            If the island's area is greater than what we have stored, update the value

        return
        """

        visited = set()
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        
        def dfs(row, col):
            if (row < 0 or col < 0 or row >= rows or col >= cols 
            or grid[row][col] != 1 or (row, col) in visited):
                return 0
            else:
                visited.add((row, col))
                return (1 + dfs(row + 1, col) + dfs(row - 1, col) 
                    + dfs(row, col + 1) + dfs(row, col - 1))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    curr_area = dfs(row, col)
                    max_area = max(curr_area, max_area)

        return max_area
                    

