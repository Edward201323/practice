class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        s = []
        for i in range(0, len(temperatures)):
            curr = temperatures[i]
            while len(s) > 0:
                peek_index = s[-1]
                peek_value = temperatures[peek_index]
                if curr > peek_value:
                    sol[peek_index] = i - peek_index
                else:
                    break
                s.pop()
            
            s.append(i)
    

        return sol
                