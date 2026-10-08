class Solution:
    def reverseVowels(self, s: str) -> str:
        mod = list(s)
        i = 0
        j = len(s) - 1
        while i <= j:
            while mod[i].lower() not in "aeiou" and i < len(s) - 1:
                i += 1
            while mod[j].lower() not in "aeiou" and j >= 0:
                j -= 1
            if i <= j:
                mod[i], mod[j] = mod[j], mod[i]
            i += 1
            j -= 1
        return "".join(mod)
