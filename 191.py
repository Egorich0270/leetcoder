class Solution:
    def hammingWeight(self, n: int) -> int:
        a = 0
        while n != 0:
            b = n // 2
            if n % 2 == 0:
                n = b
            else:
                n = b
                a += 1
        return a


print(Solution().hammingWeight(int('11111111111111111111111111111101')))
