class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        insert = n - 1
        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                res[insert] = nums[right] ** 2
                right -= 1
            else:
                res[insert] = nums[left] ** 2
                left += 1
            insert -= 1
        return res
