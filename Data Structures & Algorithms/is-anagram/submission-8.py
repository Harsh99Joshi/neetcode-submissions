class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force solution: O()
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            if t[i] in s:
                s = s.replace(t[i], "", 1)
        
        if len(s) == 0:
            return True
        else:
            return False
