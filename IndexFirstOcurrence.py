class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1 
        l, r = 0, len(needle) - 1
        res = -1
        while r < len(haystack):
            if needle == haystack[l:r+1]:
                res = l
                break
            r += 1
            l += 1
        return res
