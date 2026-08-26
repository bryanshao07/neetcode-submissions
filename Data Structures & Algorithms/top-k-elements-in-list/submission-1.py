class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        for num in nums:
            vals[num] = vals.get(num, 0)+1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in vals.items():
            buckets[value].append(key)
        ans = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans