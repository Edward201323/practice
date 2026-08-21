class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        return min(self.memoization(0, cost, cache), self.memoization(1, cost, cache))
        
    def memoization(self, s, cost, cache):
        if s >= len(cost):
            return 0
        if s in cache:
            return cache[s]
        
        cache[s] = cost[s] + min(self.memoization(s + 1, cost, cache),
        self.memoization(s + 2, cost, cache))

        return cache[s]
        