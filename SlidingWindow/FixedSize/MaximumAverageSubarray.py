class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = deque()
        n = len(nums)
        curr_sum = 0
        res = 0
        for i in range(n):
            curr.append(nums[i])
            curr_sum += nums[i]
            if len(curr) >= k:
                if len(curr) > k:
                    remove = curr.popleft()
                    curr_sum -= remove
                newRes = curr_sum / k
                if newRes > res or res == 0:
                    res = newRes
        return res
