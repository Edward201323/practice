class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        maxOdd = 0
        maxEven = 0
        for val in freq.values():
            if val > maxOdd and val % 2 == 1:
                maxOdd = val
            elif val > maxEven and val % 2 == 0:
                maxEven = val
        
        return maxOdd - maxEven