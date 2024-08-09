class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        c = 0
        if len(grid) < 2 or len(grid[0]) < 2:
            return 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 5:
                    row_sum = 15
                    if (grid[i + 1][j + 1] + grid[i - 1][j - 1] + grid[i][j] == row_sum) and\
                    (grid[i - 1][j - 1] + grid[i + 1][j + 1] + grid[i][j] == row_sum) and\
                    (grid[i+ 1][j + 1] + grid[i][j + 1] + grid[i-1][j + 1] == row_sum )and\
                    (grid[i + 1][j] + grid[i][j] + grid[i - 1][j] == row_sum) and\
                    (grid[i+ 1][j - 1] + grid[i][j - 1] + grid[i - 1][j - 1] == row_sum) and\
                    (grid[i + 1][j + 1] + grid[i + 1][j] + grid[i + 1][j - 1] == row_sum) and\
                    (grid[i][j + 1] + grid[i][j] + grid[i][j - 1] == row_sum) and\
                    (grid[i - 1][j + 1] + grid[i - 1][j] + grid[i - 1][j - 1] == row_sum):
                        c += 1
        return c

print(Solution().numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))