class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = list(nums)
        for i in range(1,len(nums)):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        minus = 0
        if left > 0:
            minus = self.nums[left-1]
        return self.nums[right] - minus
