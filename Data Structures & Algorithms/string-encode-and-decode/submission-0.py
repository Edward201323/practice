class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for s in strs:
            sol = sol + str(len(s)) + '%' + s
        return sol


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return [""]
        
        sol = []

        i = 0
        while i < len(s):
            j = i
            s_length = ""
            while s[j] != '%':
                s_length += str(s[j])
                j += 1
            j += 1

            s_length = int(s_length)

            sol_i = ""
            while s_length > 0:
                sol_i += s[j]
                s_length -= 1
                j += 1
            
            sol.append(sol_i)
            i = j
        
        return sol