class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        idxs,idxi = 0,1
        
        while idxi < len(nums):
            if nums[idxi] != 0 and nums[idxs] == 0:
                nums[idxi], nums[idxs] = nums[idxs], nums[idxi]
                idxs += 1
            elif nums[idxi] == 0 and nums[idxi-1] != 0:
                idxs = idxi
            idxi += 1
