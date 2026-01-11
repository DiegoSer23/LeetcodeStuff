class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idxs = 0
        if len(s) == 0:
            return True

        for i, val in enumerate(t):
            if val == s[idxs]:
                idxs += 1
            if idxs == len(s):
                return True
        
        return False
