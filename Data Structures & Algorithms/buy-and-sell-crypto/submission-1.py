class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max = 0
        while r < len(prices):
            curr_price = prices[r] - prices[l]
            if curr_price > max:
                max = curr_price

            if prices[r] < prices[l]:
                l = r

            r += 1

        return max