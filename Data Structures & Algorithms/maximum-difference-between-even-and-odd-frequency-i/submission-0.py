class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        a = max(freq.values())
        findMaxEven = True
        if a % 2 == 0:
            findMaxOdd = False
        
        b = 0
        for val in freq.values():
            if val > b and findMaxEven and val % 2 == 0:
                b = val
            elif val > b and not findMaxEven and val % 2 == 1:
                b = val
        
        return abs(a - b)