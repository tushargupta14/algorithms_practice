# Leetcode: https://leetcode.com/problems/evaluate-division/
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def DFS(s, e, visited) -> float:
            #print('s: ', s, 'e: ',e)
            
            if s == e: 
                return adj[s][e]
            visited.add(s)
            for j in range(m):
                if adj[s][j] !=-1.0 and j not in visited: 
                    if j == e: 
                        return adj[s][j]
                    else:
                        temp =  adj[s][j] * DFS(j, e, visited)
                        if temp >= 0: 
                            return temp
            
            return -1.0

        # adjacency matrix
        nodes = set()
        for e in equations:
            nodes.add(e[0]) 
            nodes.add(e[1])
        m = len(list(nodes))
        nodes = list(nodes)

        nodeMap = {v:i for i,v in enumerate(nodes)}

        adj = [[-1.0 for i in range(m)] for k in range(m)]
        

        for i, v in enumerate(equations): 
            adj[nodeMap[equations[i][0]]][nodeMap[equations[i][1]]] = values[i]
            adj[nodeMap[equations[i][1]]][nodeMap[equations[i][0]]] =  1/values[i]
            
            adj[nodeMap[equations[i][0]]][nodeMap[equations[i][0]]] = 1.0
            adj[nodeMap[equations[i][1]]][nodeMap[equations[i][1]]] = 1.0
  
        ans = []
        for q in queries: 
            start = q[0]
            end = q[1]
            if start not in nodeMap or end not in nodeMap: 
                ans.append(-1)
                continue
            visited = set()
            res = DFS(nodeMap[start], nodeMap[end], visited)
            ans.append(res)

        return ans