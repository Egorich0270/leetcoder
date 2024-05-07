class Solution:
    def maxArea(self, height: list[int]) -> int:
        p1 = 0
        l = len(height) - 1
        p2 = l
        s = max(0, l * min(height[p1], height[p2]))
        while p1 + 1 != p2:
            s = max(s, l * min(height[p1], height[p2]))
            l -= 1
            if l * max(height[p1 + 1], height[p2]) >= l * max(height[p1], height[p2 - 1]):
                p1 += 1
            else:
                p2 -= 1

        return max(s, l * min(height[p1], height[p2]))

print(Solution().maxArea([1,3,2,5,25,24,5]))