class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(n.bit_length()):
            if n%2 == 1:
                res += 1
            n = n >> 1
        return res
