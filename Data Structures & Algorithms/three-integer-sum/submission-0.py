class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and nums[i-1] == val:
                continue
            left = i+1
            right = len(nums)-1
            target = -1 * val
            while left < right:
                curr = nums[left]+nums[right]
                if curr > target:
                    right -=1
                elif curr < target:
                    left +=1
                else:
                    ans.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return ans