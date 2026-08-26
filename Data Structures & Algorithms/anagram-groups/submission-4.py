class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vals = {}
        for word in strs:
            freq_dict = [0] * 26
            for char in word:
                freq_dict[ord(char)-97]+=1
            freq_array = tuple(freq_dict)
            if freq_array in vals:
                vals[freq_array].append(word)
            else:
                vals[freq_array] = [word]
        ans = []
        for key, value in vals.items():
            ans.append(value)
        return ans
        