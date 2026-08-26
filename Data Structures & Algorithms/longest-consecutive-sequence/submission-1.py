class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        ans = 0
        for num in vals:
            if (num-1) not in vals:
                currVal = num+1
                currLen = 1;
                while currVal in vals:
                    currLen +=1
                    currVal +=1
                ans = max(ans, currLen)
        return ans