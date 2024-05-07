class Solution(object):
    def rob(self, nums):
        rob, no_rob = 0, 0
        for num in nums:
            rob, no_rob = no_rob + num, max(no_rob, rob)
        return max(rob, no_rob)

print(Solution().rob([2, 4, 1, 1, 7]))