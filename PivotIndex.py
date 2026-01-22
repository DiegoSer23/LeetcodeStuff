class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # Calculate right sum: total - left_sum - current element
            right_sum = total_sum - left_sum - nums[i]
            
            # Check if this is a pivot index
            if left_sum == right_sum:
                return i
            
            # Add current element to left sum for next iteration
            left_sum += nums[i]
        
        return -1
