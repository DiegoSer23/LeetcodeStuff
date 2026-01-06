class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        pprev = 1
        prev = 2
        res = 0
        for i in range(n-2):
            res = prev + pprev
            pprev = prev
            prev = res
        return res
