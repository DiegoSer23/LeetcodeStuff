class Solution:
    def reverseVowels(self, s: str) -> str:
        idx1 = 0
        idx2 = len(s) - 1
        result = list(s)
        vowels = "aeiou"
        while idx1 < idx2:
            if s[idx1].lower() in vowels and s[idx2].lower() in vowels:
                result[idx1], result[idx2] = result[idx2], result[idx1]
                idx1 += 1
                idx2 -= 1
            elif s[idx1].lower() in vowels:
                idx2 -= 1
            elif s[idx2].lower() in vowels:
                idx1 += 1
            else:
                idx1 += 1
                idx2 -= 1
        return ''.join(result)
