class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque(tokens)
        s = []
        while q:
            c = q.popleft()
            if c == '+':
                a = s.pop()
                b = s.pop()
                s.append(a + b)
            elif c == '-':
                a = s.pop()
                b = s.pop()
                s.append(b - a)
            elif c == '*':
                a = s.pop()
                b = s.pop()
                s.append(a * b)
            elif c == '/':
                a = s.pop()
                b = s.pop()
                s.append(int(b / a))
            else:
                s.append(int(c))
        
        return s.pop()