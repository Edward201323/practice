class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for nr, nc in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        # scan through the entire grid. if we come across a piece of land that hasn't been visited, we use bfs to add its entire island
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                
        return islands