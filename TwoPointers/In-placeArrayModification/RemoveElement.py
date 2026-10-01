class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        diff_idx = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[diff_idx], nums[i] = nums[i], nums[diff_idx]
                diff_idx += 1
        return diff_idx
