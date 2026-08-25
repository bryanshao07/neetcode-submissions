class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = {}
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
        for char in t:
            if char not in letters:
                return False
            else:
                if letters[char] == 1:
                    del letters[char]
                else:
                    letters[char] -= 1
        return not letters
