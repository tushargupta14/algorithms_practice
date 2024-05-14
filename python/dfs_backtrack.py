# Leetcode: https://leetcode.com/problems/path-with-maximum-gold/?envType=daily-question&envId=2024-05-14


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(grid, i, j, m, n):

            if i < 0 or i >= m or j < 0 or j >= n: 
                return 0
     
            if grid[i][j] == 0: 
                return 0
            temp = grid[i][j]
            grid[i][j] = 0 
            max_gold = temp + max(dfs(grid, i+1, j, m, n), 
                                  dfs(grid, i, j+1, m, n), 
                                  dfs(grid, i-1, j, m, n), 
                                  dfs(grid, i, j-1, m, n))

            grid[i][j] = temp
            return max_gold
        
        m, n = len(grid), len(grid[0])
        max_sum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_sum = max(dfs(grid, i, j, m, n), max_sum)

        return max_sum