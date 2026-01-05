class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        prev = False

        for i in range(n - 1, -1, -1):
            if not prev and i < n - 1:
                break
            if digits[i] == 9 and (prev or i == n - 1):
                digits[i] = 0
                prev = True
                if i == 0:
                    digits.insert(0, 1)
            elif prev or i == n - 1:
                digits[i] += 1
                prev = False
        return digits
