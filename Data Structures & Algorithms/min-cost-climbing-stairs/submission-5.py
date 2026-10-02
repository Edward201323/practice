class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        getminimum(cost, 0)
        getminimum(cost, i):
            if i >= len(cost):
                return 0

            current_cost = cost[i]
            one_step = getminimum(cost, i + 1)
            two_step = getminimum(cost, i + 2)
            return current_cost + min(one_step, two_step)
        """
        # cache = {}
        # def memoization(i, cache, cost):
        #     if i >= len(cost):
        #         return 0

        #     if i in cache:
        #         return cache[i]

        #     current_cost = cost[i]
        #     one = memoization(i + 1, cache, cost)
        #     two = memoization(i + 2, cache, cost)
        #     cache[i] = current_cost + min(one, two)

        #     return cache[i]

        # return min(memoization(0, cache, cost), memoization(1, cache, cost))


        # base cases: start at 0, 1
        dp = [cost[0], cost[1]]
        i = 2
        while i < len(cost):
            temp = dp[1]
            dp[1] = cost[i] + min(dp[0], dp[1])
            dp[0] = temp
            i += 1
        
        return min(dp[0], dp[1])





