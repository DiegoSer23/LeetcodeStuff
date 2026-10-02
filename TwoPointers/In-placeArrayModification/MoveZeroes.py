class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write_idx], nums[i] = nums[i], nums[write_idx]
                write_idx += 1
        return
