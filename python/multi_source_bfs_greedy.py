# Attempted not solved
# Leet Code: https://leetcode.com/problems/find-the-safest-path-in-a-grid/?source=submission-noac
from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1: 
            return 0
        n = len(grid)
        if grid[n-1][n-1] == 1:
            return 0

        mds = [[900 for i in range(n)] for j in range(n)]

        def bfs(i, j, grid, mds, q, seen, n):
        
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

        def is_valid(mds, v, n):

            seen = set()
            stack = [(0,0)]

            while (len(stack)):
                i, j = stack.pop()
                #print(i, j, mds[i][j])
                seen.add((i,j))
                if (i,j) == (n-1,n-1):
                    #print('Heren')
                    return True
                # Add the valid neighbors
                if i < n-1 and (i+1, j) not in seen and mds[i+1][j] >= v:
                    #print('Here')
                    stack.append((i+1, j))
                if i > 0 and (i-1, j) not in seen and mds[i-1][j] >= v:
                    stack.append((i-1, j))
                if j < n-1 and (i, j+1) not in seen and mds[i][j+1] >= v:
                    stack.append((i, j+1))
                if j > 0 and (i, j-1) not in seen and mds[i][j-1] >= v:
                    stack.append((i, j-1))

            return False

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    # begin BFS
                    #mds[i][j] = 0
                    q = deque()
                    q.append((i,j,0))
                    seen = set()
                    bfs(i, j, grid, mds, q, seen, n)
        
        max_val = -1
        for i in range(n):
            for j in range(n):
                max_val = max(max_val, mds[i][j])

        #safe_arr = [k for k in range(1,max_val+1)]
        left = 1
        right = max_val
        #print(mds)
        #print('max_val ', max_val)
        #print(is_valid(mds, 2, n))
        if max_val == 1:
            if is_valid(mds, 1, n):
                return 1
            else:
                return 0
        res = 0
        while(right >= left):
            mid = (right - left) // 2 + left
            # check if mid is valid
            #print(mid)
            #print('left: ', left, 'mid: ', mid, 'right: ', right)
            if is_valid(mds, mid, n):
                res = mid
                left = mid + 1
                #print(left)
            else:
                right = mid - 1
    
        return res