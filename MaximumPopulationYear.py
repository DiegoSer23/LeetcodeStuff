class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101
        for log in logs:
            years[log[0]-1950] += 1
            years[log[1]-1950] -= 1
        s = 0
        max_s = 0
        res = 0
        for i in range(len(years)):
            s += years[i]
            if s > max_s:
                max_s = s
                res = i + 1950
        return res 
