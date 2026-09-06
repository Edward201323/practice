class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in range(len(tokens) - 1, -1, -1):
            s.append(tokens[i])
        
        while len(s) > 1:
            a = int(s.pop())
            b = int(s.pop())
            char = s.pop()
            if char == '+':
                s.append(a + b)
            if s == '-':
                s.append(a - b)
            if char == '*':
                s.append(a * b)
            if char == '/':
                s.append(a / b)
        
        return s.pop()