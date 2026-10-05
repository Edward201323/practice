class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visit.add((row, col))
        
        distance = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = distance
                
                neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for n_row, n_col in neighbors:
                    if (n_row >= 0 and n_row < rows and n_col >= 0 and n_col < cols
                    and (n_row, n_col) not in visit and grid[n_row][n_col] == 2147483647):
                        q.append((n_row, n_col))
                        visit.add((n_row, n_col))

            distance += 1
