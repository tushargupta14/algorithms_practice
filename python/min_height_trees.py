"""Leetcode: 310: https://leetcode.com/problems/minimum-height-trees/description/

Returns:
    Find all the roots that build minimum height trees
    Important in learning concept of diameter and total MHTs possible == 2 at most
"""
from collections import defaultdict, deque
import math

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1: 
            return [0]
        hmap = defaultdict(list)
        for e in edges: 
            hmap[e[0]].append(e[1])
            hmap[e[1]].append(e[0])
    
        q = deque([k for k,v in hmap.items() if len(v) == 1])
        #print(q)
        while n > 2: 
            x = len(q)
            n = n - x
            for _ in range(x): 
                node = q.popleft() 
                for neighb in hmap[node]: 
                    hmap[neighb].remove(node)
                    if len(hmap[neighb]) == 1: 
                        q.append(neighb)

        return list(q)