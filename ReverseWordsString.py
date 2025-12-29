class Solution:
    def reverseWords(self, s: str) -> str:
        separate = s.split()
        res = []
        for i in reversed(separate):
            res.extend(i)
            res.append(" ")
        res.pop()
        return "".join(res)
