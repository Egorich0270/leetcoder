class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        p1 = 0
        p2 = 0
        r = 0
        c = 0
        if goal == 0:
            pass
        while c != goal:
            if nums[p2] == 1:
                c += 1
                if c == goal:
                    break
            p2 += 1
            if p2 >= len(nums) and c != goal:
                print('aaa')
                return 0

        while p2 + 1 < len(nums):
            if c == goal:
                if p1 != p2:
                    r += 1
            if nums[p2 + 1] == 1:
                if c == goal:
                    if nums[p1] == 0:
                        p1 += 1
                    else:
                        p1 += 1
                        c -= 1
                        continue
                if c < goal:
                    p2 += 1
                    c += 1
            else:
                p2 += 1

        while nums[p1] == 0:
            r += 1
            p1 += 1

        if p1 != p2:
            return r + 1
        if p1 == p2:
            return r







print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0))