class Solution:
    def numDecodings(self, s: str) -> int:
        
        def compute(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            total = compute(i + 1)


            if i + 1 < len(s) and 10 <= int(s[i] + s[i + 1]) <= 26:
                total += compute(i + 2)

            return total

        return compute(0)