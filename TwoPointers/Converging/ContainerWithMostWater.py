class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        res = 0
        while left_ptr < right_ptr:
            if (right_ptr - left_ptr) * min(height[left_ptr], height[right_ptr]) > res:
                res = (right_ptr - left_ptr) * min(height[left_ptr], height[right_ptr])
            if height[right_ptr] < height[left_ptr]:
                right_ptr -= 1
            else:
                left_ptr += 1
        return res
