class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        """
        [1, 3], [1, 5], [4, 7], [8, 9]
        first, we should sort by the 0th then first index
        
        constantly check whether the 0th index lies in between the previous range
        """

        intervals.sort()
        sol = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            previous_low = sol[-1][0]
            previous_high = sol[-1][1]
            if previous_low <= interval[0] <= previous_high:
                sol[-1][1] = interval[1] # we already know that interval[i] is <= because we sorted it
            else:
                sol.append(interval)

        return sol

                
