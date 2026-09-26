class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        res = []
        while left < right:
            sumR = numbers[left] + numbers[right]
            if sumR > target:
                right -= 1
            elif sumR < target:
                left += 1
            else:
                res = [left + 1, right + 1]
                break
        return res
