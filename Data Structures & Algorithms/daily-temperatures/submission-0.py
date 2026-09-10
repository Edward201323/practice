class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = []
        for i in range(len(temperatures)):
            curr = temperatures[i]
            j = i + 1
            while j < len(temperatures):
                if curr < temperatures[j]:
                    break
                j += 1
            
            if j >= len(temperatures):
                sol.append(0)
            else:
                sol.append(j - i)
        
        return sol

            
                