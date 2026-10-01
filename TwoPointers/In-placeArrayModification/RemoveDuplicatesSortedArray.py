class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_idx = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                nums[unique_idx] = nums[i-1]
                unique_idx += 1
        nums[unique_idx] = nums[len(nums) - 1]
        return unique_idx + 1
