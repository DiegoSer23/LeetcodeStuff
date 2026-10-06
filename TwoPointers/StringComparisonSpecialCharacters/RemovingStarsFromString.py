class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        n = len(s)
        i = n - 1
        skip = 0
        while i >= 0:
            if s[i] == "*":
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                res.append(s[i])
            i -= 1
        res.reverse()
        return "".join(res)
