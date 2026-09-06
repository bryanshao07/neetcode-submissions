class Solution:
    def calculate(self, s: str) -> int:
        curr = 0
        op = '+'
        stack = []
        s = s.replace(" ", "")
        for i, ch in enumerate(s):
            if ch.isdigit():
                curr = curr*10 + int(ch)
            if ch in '+-*/' or i == len(s)-1:
                if op == '+':
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == "*":
                    temp = stack.pop()
                    stack.append(temp*curr)
                else:
                    temp = stack.pop()
                    stack.append(int(temp/curr))
                op = ch
                curr = 0
        
        return sum(stack)
        