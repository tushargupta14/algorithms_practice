# Leetcode: Network delay time

import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        dist = [-1] * n
        for el in times: 
            adj[el[0]].append((el[1], el[2]))
        
        seen = set()
        
        heap = []
        heapq.heappush(heap, (0, k))
        dist[k-1] = 0
        while(heap): 
            # pop the element with the smallest distance from source
            el = heapq.heappop(heap)
            node = el[1]
            #print('node', node)
            if node in seen: 
                continue
            
            for u, t in adj[node]: 
                if u not in seen:
                    
                    if dist[u-1] == -1: 
                        dist[u-1] = el[0] + t
                    elif dist[u-1] > el[0] + t: 
                        dist[u-1] = el[0] + t
                    #print(u, dist[u-1])
                    heapq.heappush(heap, (dist[u-1], u))
            
            seen.add(node)
        #print(dist)
        for j in range(n): 
            if dist[j] == -1: 
                return -1
        
        return max(dist)
        
        