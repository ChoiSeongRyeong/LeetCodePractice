class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        r_max = [max(row) for row in grid]
        c_max = [max(col) for col in list(zip(*grid))]

        return sum([
            sum([
                min(r_max[r], c_max[c]) - grid[r][c]
                for r in range(n)
            ])
            for c in range(n)
        ])