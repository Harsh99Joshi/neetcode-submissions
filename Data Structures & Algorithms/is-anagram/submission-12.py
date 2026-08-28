class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        
        for char in t:
            if char not in d or d[char] == 0:
                return False
            elif d[char] > 0:
                d[char] -= 1

        return False if (any(v > 0 for v in d.values())) else True
        
        
        # #brute force solution: O(n^2) because iteration + replacing
        # if len(s) != len(t):
        #     return False
        # for i in range(len(t)):
        #     if t[i] in s:
        #         s = s.replace(t[i], "", 1)
        
        # if len(s) == 0:
        #     return True
        # else:
        #     return False
