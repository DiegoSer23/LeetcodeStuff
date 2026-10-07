class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def getPalindromes(right: int, left: int):
            nonlocal res
            r, l = right, left
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            getPalindromes(i, i)
            getPalindromes(i + 1, i)
        return res
