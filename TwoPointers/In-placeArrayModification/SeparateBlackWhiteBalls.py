class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "0":
                res += (i - left)
                left += 1
        return res
