class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []
        for char in s:
            if char not in match:
                stack.append(char)
            else:
                if not stack or stack[-1] != match[char]:
                    return False
                else:
                    stack.pop()
        return not stack