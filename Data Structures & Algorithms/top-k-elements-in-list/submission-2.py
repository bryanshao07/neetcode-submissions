class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        counts = [[] for i in range(len(nums)+1)]

        for n in nums:
            map[n] = 1 + map.get(n, 0)
        for key, val in map.items():
            counts[val].append(key)
        ret = []
        for i in range(len(counts)-1, 0, -1):
            for n in counts[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret