class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        last_valid = 0
        while low <= high:
            bPerHour = (low + high) // 2
            currHours = 0
            for pile in piles:
                currHours += math.ceil(pile / bPerHour)
            
            if currHours <= h:
                high = bPerHour - 1
                last_valid = bPerHour
            else:
                low = bPerHour + 1
                
        return last_valid