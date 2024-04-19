# https://leetcode.com/problems/number-of-islands/?envType=daily-question&envId=2024-04-19
# Grid based dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()
        islands = 0 

        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j, seen, m, n):

            if (i,j) in seen: 
                return 
                
            seen.add((i,j))
            #print('m', m, 'n', n)
            #print(i,j)
            if int(grid[min(i+1, m-1)][j]): 
                dfs(grid, min(i+1, m-1), j, seen, m, n)

            if  int(grid[i][min(j+1, n-1)]): 
                dfs(grid, i, min(j+1, n-1), seen, m, n)

            if int(grid[max(i-1, 0)][j]): 
                dfs(grid, max(i-1, 0), j, seen, m, n)

            if int(grid[i][max(j-1, 0)]): 
                dfs(grid, i, max(j-1, 0), seen, m, n)

            return

        for i in range(m): 
            for j in range(n): 

                # Start dfs if not visited
                #print(seen)
                if (i,j) not in seen and int(grid[i][j]): 
                    #print('i ', i, 'j ', j)
                    dfs(grid, i, j, seen, m, n)
                    islands+=1

        return islands