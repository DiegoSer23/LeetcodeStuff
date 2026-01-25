class Solution:
    def quickSort(self, s: str) -> str:
        if len(s) < 1:
            return s
        left = []
        equal = []
        right = []
        pivot = s[0]
        for i in range(len(s)):
            if s[i] < pivot:
                left.append(s[i])
            elif s[i] == pivot:
                equal.append(s[i])
            else:
                right.append(s[i])
        return self.quickSort(left)+equal+self.quickSort(right)

    def isAnagram(self, s: str, t: str) -> bool:
        if self.quickSort(s) == self.quickSort(t):
            return True
        else:
            return False
