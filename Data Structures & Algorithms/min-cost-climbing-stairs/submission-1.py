class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.memoization(0, cost, {}), self.memoization(1, cost, {}))

    def memoization(self, step, cost, cache):
        if step >= len(cost):
            return 0
        if step in cache:
            return cache[step]
        
        cache[step] = cost[step] + min(self.memoization(step + 1, cost, cache), 
        self.memoization(step + 2, cost, cache))
        
        return cache[step]

