class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.dfs(0, cost), self.dfs(1, cost))
    
    def dfs(self, i, cost):
        if i >= len(cost):
            return 0
        return cost[i] + min(self.dfs(i + 1, cost), self.dfs(i + 2, cost))