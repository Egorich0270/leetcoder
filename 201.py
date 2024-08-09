class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        res = 0
        tokens.sort()
        p1 = 0
        p2 = len(tokens) - 1
        while p1 < p2:
            if tokens[p1] <= power:
                power -= tokens[p1]
                res += 1
                p1 += 1
                continue
            else:
                power += tokens[p2]
                p2 -= 1
                res -= 1

            pass
        if p1 == p2:
            if power >= tokens[p1]:
                res += 1
        if res >= 0:
            return res
        else:
            return 0


print(Solution().bagOfTokensScore([55,71,82], 54))