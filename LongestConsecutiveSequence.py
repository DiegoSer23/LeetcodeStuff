class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        length = 0
        max_length = 0
        for item in seen:
            if item - 1 in seen:
                continue
            length += 1
            while item + length in seen:
                length += 1
            if length > max_length:
                max_length = length
            length = 0
        return max_length
