class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        # optimize by looking at neighbor values
        bfs(row, col):
            variable that holds the distance from our original cell
            have a set that contains visited cells
            dequeue that holds that holds neighbors that we need to visit next
            append our original cell to our dequeue
            while dequeue exists:
                curr = dequeue.popleft()
                if the current cell is == 0:
                    return our distance variable
                if the current cell is != INF, 0, or -1:
                    return the cells value + our distance variable

                add all of its valid neighbors (in bounds, the neighbor cell can't have -1, hasnt been visited)
                update visit
                increment our distance variable by one


        traverse throughout the graph:
            if the current cell != -1 and 0:
                perform BFS on this cell, to find the nearest treasurechest
        """



        rows = len(grid)
        cols = len(grid[0])

        def bfs(original_row, original_col):
            visit = set()
            q = deque()
            q.append((original_row, original_col, 0))
            visit.add((original_row, original_col))
            while q:
                row, col, distance = q.popleft()
                if grid[row][col] == 0:
                    return distance
                
                neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for n_row, n_col in neighbors:
                    if (n_row >= 0 and n_row < rows and n_col >= 0 and n_col < cols
                    and grid[n_row][n_col] != -1 and (n_row, n_col) not in visit):
                        q.append((n_row, n_col, distance + 1))
                        visit.add((n_row, n_col))
                distance += 1
            
            return 2147483647

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2147483647:
                    grid[row][col] = bfs(row, col)








