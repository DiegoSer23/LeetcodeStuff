class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxavg = 0
        maxsum = 0
        for i in range(len(nums)):
            if i < k:
                maxsum += nums[i]
            if i == k - 1:
                maxavg = maxsum / k
            if i >= k:
                newavg = (maxsum - nums[i-k] + nums[i]) / k
                maxsum = maxsum - nums[i-k] + nums[i]
                if newavg > maxavg:
                    maxavg = newavg
            
        return maxavg
