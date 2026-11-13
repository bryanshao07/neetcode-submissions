class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = collections.defaultdict(list)
        for s in strs:
            word_freq = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                word_freq[index] +=1
            freq_map[tuple(word_freq)].append(s)
        ret = []
        return list(freq_map.values())