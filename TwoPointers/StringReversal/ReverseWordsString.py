class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i = j = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                j += 1
            else:
                while j < len(s) and s[j] != " ":
                    j += 1
                res.append(s[i:j])
                i = j
        return " ".join(reversed(res))
