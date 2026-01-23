class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        newsum = 0
        while n != 1:
            while n!= 0:
                newsum += (n%10) ** 2
                n //= 10
            if newsum in seen:
                return False
            else:
                seen.add(newsum)
            n = newsum
            newsum = 0
        return True
