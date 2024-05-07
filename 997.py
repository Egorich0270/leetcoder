class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        relationship = [[0] * n, [0] * n]
        for x in trust:
            relationship[0][x[0]-1] += 1
            relationship[1][x[1]-1] += 1
        for i, x in enumerate(relationship[0]):
            if x == 0:
                if relationship[1][i] == n-1:
                    return i + 1

        return -1
