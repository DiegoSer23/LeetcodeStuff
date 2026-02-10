class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
            if nums[i] == 1:
                white += 1
        nums[0:red] = [0] * (red)
        nums[red:white+red] = [1] * (white)
        nums[white+red:len(nums)] = [2] * (len(nums) - (white + red))
