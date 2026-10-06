class Solution:
    def minOperations(self, logs: list[str]) -> int:
        res = 0
        for i, val in enumerate(logs):
            if val == "../" and res > 0:
                res -= 1
            elif val == "./":
                continue
            elif val != "../" and val != "./":
                res += 1
        return res
