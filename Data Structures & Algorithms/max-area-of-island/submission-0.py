class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Plan:
        Itterate throughout the graph
            If I come across a unvisited 1, run BFS on the island to get the area
            If the island's area is greater than what we have stored, update the value

        return
        """

        visited = set()
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def bfs(row, col):
            q = collections.deque()
            curr_area = 0
            q.append((row, col))
            visited.add((row, col))

            while q:
                row, col = q.popleft()
                visited.add((row, col))
                curr_area += 1
                new_tiles = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for nr, nc in new_tiles:
                    if (nr < rows and nc < cols and nr >= 0 and nc >= 0
                    and (nr, nc) not in visited and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return curr_area


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    curr_area = bfs(row, col)
                    max_area = max(curr_area, max_area)

        return max_area
                    

