class Solution:
    def canSortArray(self, nums: list[int]) -> bool:

        for _ in range(len(nums)):
            numbers_swapped = False
            for number_index in range(len(nums) - 1):

                if nums[number_index] > nums[number_index + 1]:

                    if nums[number_index].bit_count() == nums[number_index + 1].bit_count():

                        nums[number_index], nums[number_index + 1] = nums[number_index + 1], nums[number_index]
                        numbers_swapped = True
                    else:
                        return False
            if not numbers_swapped:
                return True
        return True

assert (Solution().canSortArray([3,16,8,4,2])) == False
assert (Solution().canSortArray([1,2,3,4,5])) == True
assert (Solution().canSortArray([8,8,2,30,15])) == True