class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                del seen[nums[i]]
        return next(iter(seen))
