class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        maxOdd = 0
        minEven = max(freq.values())
        for val in freq.values():
            if val > maxOdd and val % 2 == 1:
                maxOdd = val
            elif val < minEven and val % 2 == 0:
                minEven = val
        
        return maxOdd - minEven