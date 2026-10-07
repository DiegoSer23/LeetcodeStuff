class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            #odd
            r = l = i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                r += 1
                l -= 1
            #even
            r, l = i + 1, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                r += 1
                l -= 1
        return res
