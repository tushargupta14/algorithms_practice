# Leetcode: Island Perimeter
# https://leetcode.com/problems/island-perimeter/?envType=daily-question&envId=2024-04-18
class Solution:


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        

        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j, m, n): 
            
            #print('i', i,'j', j)

            if i<0 or i >= m or j<0 or j>=n: 
                return 1

            if grid[i][j] == -1: 
                # node visited
                return 0

            if grid[i][j] == 0 : 
                return 1 
            
            # node visited
            grid[i][j] = -1
            ans = 0 
            ans+= dfs(grid, i+1, j, m, n)
            ans+= dfs(grid, i-1, j, m, n)
            ans+= dfs(grid, i, j+1, m, n)
            ans+= dfs(grid, i, j-1, m, n)
            #print('ans', ans)
            return ans

        ans = 0 
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 1:
                    #print('start', i, j) 
                    ans = dfs(grid, i, j, m, n)
                    break
        
        return ans