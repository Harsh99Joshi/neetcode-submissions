from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_list = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key not in anagrams_list:
                anagrams_list[key] = []
            anagrams_list[key].append(s)

        
        return list(anagrams_list.values())