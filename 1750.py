class Solution:
    def minimumLength(self, s: str) -> int:
        p2 = len(s) - 1
        p1 = 0
        while p1 < p2:
            if s[p1] == s[p2]:
                char = s[p1]
                while p1 < p2 and (s[p1] == char or s[p2] == char):
                    if s[p1] == char:
                        p1 += 1
                    else:
                        p2 -= 1
            else:
                break
        if p1 > p2:
            return 0

        return p2 - p1 + 1

print(Solution().minimumLength('cabaabac'))
