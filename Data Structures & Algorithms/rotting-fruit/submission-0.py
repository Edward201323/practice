class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        0: empty cell
        1: fresh fruit
        2: rotten fruit

        important notes:
        I can see right away that if theres a 1 surrounded by 0's, we have to return -1
        I'm going to use bfs to traverse the graph, starting from the rotton fruits

        a set to see if every fruit is rotten at the end of the bfs
        a set to denote the fruits that i'm going to visit/visited
        queue to store all of the fruits that are rotten/going to become rotten
        a variable to keep track of the time/solution

        traverse the entire grid:
            if the current cell is a fresh fruit:
                put it inside of the fresh fruits set
            if the current cell is a rotten fruit:
                put it in side of the bfs queue
                put it inside the visit/visited fruits set

        while q isn't empty and fruits set isn't empty:
            for in range len(q):
                curr = q.popleft()
                if neighbor is in bounds and a fresh fruit:
                    remove the fresh fruit from the fresh fruits set
                    add the neighbor to the fresh fruits set
                    set the neighbor as rotten
            
            increment the time

        if fruits in fruit set:
            return -1
        else:
            retunr the time

        """

        rows, cols = len(grid), len(grid[0])
        fresh = set()
        visit = set()
        new_rotten = deque()
        time = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh.add((row, col))
                elif grid[row][col] == 2:
                    new_rotten.append((row, col))
                    visit.add((row, col))
        
        while new_rotten and fresh:
            for i in range(len(new_rotten)):
                row, col = new_rotten.popleft()
                neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for n_row, n_col in neighbors:
                    if (n_row >= 0 and n_row < rows and n_col >= 0 and n_col < cols
                    and (n_row, n_col) not in visit and grid[n_row][n_col] == 1):
                        grid[n_row][n_col] = 2
                        new_rotten.append((n_row, n_col))
                        fresh.remove((n_row, n_col))


            time += 1
        
        if fresh:
            return -1
        else:
            return time




