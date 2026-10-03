class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def memoization(i, s, cache):
            if i in cache:
                return cache[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0

            ways = memoization(i + 1, s, cache)

            if i < len(s) - 1 and 10 <= int(s[i] + s[i + 1]) <= 26:
                ways += memoization(i + 2, s, cache)
            
            cache[i] = ways
            return ways

        return memoization(0, s, cache)