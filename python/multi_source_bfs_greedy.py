# Attempted not solved, MLE 
# Solutions do not create an mds new grid. Modify grid in-place
# Leet Code: https://leetcode.com/problems/find-the-safest-path-in-a-grid/?source=submission-noac
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1: 
            return 0
        n = len(grid)
        if grid[n-1][n-1] == 1:
            return 0

        #mds = [[900 for i in range(n)] for j in range(n)]

        
        def bfs(grid, mds, q, seen, n):
            while(len(q)):
                i, j, d = q.popleft()
                mds[i][j] = min(mds[i][j], d)
                seen.add((i,j))
                # reach all 4 neighbors
                if i < n-1 and (i+1, j) not in seen:
                    q.append((i+1, j, d+1))
                if i > 0 and (i-1, j) not in seen:
                    q.append((i-1, j, d+1))
                if j < n-1 and (i, j+1) not in seen:
                    q.append((i, j+1, d+1))
                if j > 0 and (i, j-1) not in seen:
                    q.append((i, j-1, d+1))

        seen = set()
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    # begin BFS
                    #mds[i][j] = 0
                    q.append((i,j,0))
                    seen.add((i,j))

        bfs(grid, mds, q, seen, n)
        #print(mds)
        # Djikstra's algorithm
        h = [(-mds[0][0], 0, 0)]
        heapq.heapify(h)
        min_val = mds[0][0]
        seen = set((i,j))
        dirs = [(0,-1), (-1, 0), (1,0), (0,1)]
        while(h):
            dist, i, j = heapq.heappop(h)
            #print(dist, i, j)
            min_val = min(-dist, min_val)
            if (i, j) == (n-1, n-1):
                return min_val
            
            seen.add((i,j))

            for direc in dirs:
                x, y = i + direc[0], j + direc[1]
                if n > x >=0 and n> y >=0 and (x,y) not in seen:
                    heapq.heappush(h, (-mds[x][y], x, y)) 
            
        return min_val

       