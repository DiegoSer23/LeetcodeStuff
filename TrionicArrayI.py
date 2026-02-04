class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p, q, i = -1, -1, 1
        while p == -1 and i < len(nums):
            if nums[i-1] == nums[i]:
                return False
            if nums[i-1] < nums[i]:
                i += 1
            else:
                if i - 1 == 0:
                    return False
                p = i - 1
        i = p + 1
        while q == -1 and i < len(nums):
            if nums[i-1] == nums[i]:
                return False
            if nums[i-1] > nums[i]:
                i += 1
            else:
                q = i - 1
        if q == -1:
            return False
        while i < len(nums):
            if nums[i-1] == nums[i]:
                return False
            if nums[i-1] > nums[i]:
                return False
            else:
                i += 1

        if q > p and p > 0 and q < len(nums) - 1:
            return True
        else:
            return False   
