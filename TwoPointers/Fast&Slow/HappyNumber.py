class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sumI = n
        while sumI != 1:
            numI = sumI
            sumI = 0
            for digit in str(abs(numI)):
                sumI += int(digit) ** 2
            if sumI in seen:
                return False
            else:
                seen.add(sumI)
        return True
