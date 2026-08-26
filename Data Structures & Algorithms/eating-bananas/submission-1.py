class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bPerHour = 1

        while True:
            currHours = 0
            for b in piles:
                currHours += math.ceil(b / bPerHour)
            
            if currHours <= h:
                return bPerHour
            
            bPerHour += 1
        
        return -1