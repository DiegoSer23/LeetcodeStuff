class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        if gain[0] > res:
            res = gain[0]

        for i in range(1,len(gain)):
            if i == 1:
                curr_gain = gain[i-1] + gain[i]
            else:
                curr_gain += gain[i]
            if curr_gain > res:
                res = curr_gain
        
        return res
