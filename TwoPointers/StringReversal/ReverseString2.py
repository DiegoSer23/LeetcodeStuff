class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)
        i = 0
        j = k - 1
        mult = 1
        while j < len(s):
            while i <= j:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
            i = (2 * k) * mult
            j = i + k - 1
            mult += 1
        if len(s) - i < k:
            j = len(s) - 1
            while i <= j:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
        return "".join(res)
