class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        for char in t:
            if char not in dic or dic[char] == 0:
                return False
            dic[char] -= 1

        

        return True