class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1: island
        2: water

        bfs(row, col):
            create a queue
            add (row, col) to the queue
            while the q exists:
                pop the left of the queue, mark it as the current index
                set the current index in grid to zero, so we dont visit it again
                add current index's neighbors to the queue
                    make sure the neighbors fit within the grid, and that their values are equal to "1"

        itterate through the grid:
            if curr == "1":
                bfs the entire island: to set every single piece of the island as one
                
        """

        rows, cols = len(grid), len(grid[0])
        sol = 0
        
        def bfs(start_row, start_col):
            q = deque()
            q.append((start_row, start_col))
            while q:
                row, col = q.popleft()
                grid[row][col] = "0"

                # add the neighbors
                neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for new_row, new_col in neighbors:
                    if (0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1"):
                        q.append((new_row, new_col))



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    sol += 1

        return sol
        
        





