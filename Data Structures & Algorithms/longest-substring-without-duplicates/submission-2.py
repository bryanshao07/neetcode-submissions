class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        right = 0
        curr_set = set()
        while right < len(s):
            if (s[right] not in curr_set):
                curr_set.add(s[right])
                right +=1
                max_length = max(max_length, right-left)
            else:
                curr_set.remove(s[left])
                left += 1
        return max_length