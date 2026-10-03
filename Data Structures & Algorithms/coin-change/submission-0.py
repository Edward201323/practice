class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        given the money in coins, whats the fewest number of coins needed to make the exact target amount

        bottom up:
        memoization(curr, coins, cache, target):
            if curr in cache:
                return curr[i]
            if the curr is < 0:
                we didn't find a valid amount of coins
                return -1
            if curr == 0:
                we found a valid combination
                return: amount of coins
            
            for coins:
                recursively call: memoization(curr -= coin)
            
            cache[curr] = amount of coins

            retrun minimum of our decision trees
            
        """
        if amount == 0:
            return 0

        cache = {}
        def memoization(target):
            if target in cache:
                return cache[target]
            if target < 0:
                return -1
            if target == 0:
                return 0

            # Make sure to account for the case in which the solution is = -1
            
            minimum = target + 1 # max amount of coins needed is amount
            for coin in coins:
                curr = memoization(target - coin)
                if curr < minimum and curr >= 0:
                    minimum = curr
                
            if minimum == target + 1:
                return -1
            
            cache[target] = minimum + 1
            
            return cache[target]            

        return memoization(amount)
