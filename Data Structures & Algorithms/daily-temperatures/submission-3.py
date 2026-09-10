class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        s = []

        for i in range(0, len(temperatures)):
            curr = temperatures[i]
            while len(s) > 0 and curr > temperatures[s[-1]]:
                sol[s[-1]] = i - s[-1]
                s.pop()
            
            s.append(i)
    

        return sol
                