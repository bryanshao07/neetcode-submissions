class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ret = [0] * (2*len(nums))
        for i in range(len(nums)):
            ret[i] = nums[i]
            ret[i+len(nums)] = nums[i]
        return ret 