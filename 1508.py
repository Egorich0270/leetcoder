class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        start_sum = [0] * (n * (n + 1) // 2)
        c = 0
        for i in range(n):
            c += nums[i]
            start_sum[i] = c
        for i in range(n):
            for j in range(i + 1, n):
                start_sum[(n * (i + 1) - ((i + 1) * i // 2)) + n - j - 1] = start_sum[(n - j ) + ((n * (i) - ((i - 1) * i // 2)))] - nums[i]

        start_sum.sort()
        return sum(start_sum[left - 1:right:]) % (100000007)


print(Solution().rangeSum([1,2,3,4], 4, 1, 5))