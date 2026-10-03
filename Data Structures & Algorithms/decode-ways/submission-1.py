class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def memoization(i, s):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0

            ways = memoization(i + 1, s)

            if i < len(s) - 1 and 10 <= int(s[i] + s[i + 1]) <= 26:
                ways += memoization(i + 2, s)
            
            return ways

        return memoization(0, s)