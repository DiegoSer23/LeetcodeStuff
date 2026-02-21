class Solution:
    def countBitsCheckPrime(self, num) -> int:
        count = 0
        while num > 0:
            if num % 2 == 1:
                count += 1
            num = num // 2
        if count <= 1:
            return 0
        i = 2
        while i * i <= count:
            if count % i == 0:
                return 0
            i += 1
        return 1

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            count += self.countBitsCheckPrime(i)
        return count
