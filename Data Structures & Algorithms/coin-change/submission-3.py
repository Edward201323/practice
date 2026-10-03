class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def memoization(curr):
            if curr in cache:
                return cache[curr]
            if curr == 0:
                return 0
            if curr < 0:
                return -1
            
            minimum = float('inf')
            for coin in coins:
                i = memoization(curr - coin)
                if i >= 0 and i < minimum:
                    minimum = i
            
            if minimum == float('inf'):
                cache[curr] = -1
                return -1
            else:
                cache[curr] = minimum + 1
                return cache[curr]
        
        return memoization(amount)
            


            
            