class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bPerHour = 1
        
        currHours = 0
        while currHours < h:
            currHours = 0
            for b in piles:
                currHours += math.ceil(b / bPerHour)

            bPerHour += 1

        return bPerHour - 1