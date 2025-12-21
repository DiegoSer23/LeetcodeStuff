class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count2 = 0
        count1 = 0
        result = ""
        while count1 < len(word1) or count2 < len(word2):
            if count1 < len(word1) and count2 < len(word2):
                result += word1[count1]
                result += word2[count2]
                count1 += 1
                count2 += 1
            elif count1 < len(word1):
                result += word1[count1]
                count1 += 1
            elif count2 < len(word2):
                result += word2[count2]
                count2 += 1
        return result
