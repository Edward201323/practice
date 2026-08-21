class Solution:
    def climbStairs(self, n: int) -> int:
        return self.memoization(n, {})

    def memoization(self, n, cache):
        if n <= 2:
            return n
        if n in cache:
            return cache[n]

        cache[n] = self.memoization(n - 1, cache) + self.memoization(n - 2, cache)
        return cache[n]
