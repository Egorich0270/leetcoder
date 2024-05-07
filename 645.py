from collections import Counter
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        c = Counter(nums)
        for x in range(1, len(nums)+1):
            if c.get(x):
                if c[x] == 2:
                    a = x
            else:
                b = x
        return [a, b]


print(Solution().findErrorNums([1,2,1,3,4,5]))