class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        new_slow = 0
        while new_slow != slow:
            slow = nums[slow]
            new_slow = nums[new_slow]
        return slow
