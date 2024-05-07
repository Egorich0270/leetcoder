class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        num = 0
        char = nums[0]
        for x in nums:
            if x == char:
                num += 1
            else:
                if num == 0:
                    char = x
                else:
                    num -= 1
        return char