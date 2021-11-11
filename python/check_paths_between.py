#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11-11-2021 16:27
# @Author  : Tushar Gupta

from collections import defaultdict


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    # Do not use recursion
    def DFS(self, source, end, adj, visited):

        # if source in visited:
        #     return False

        visited.add(source)

        for node in adj[source]:
            if node not in visited:
                print(node, end)
                if node == end:
                    return True
                else:
                    return self.DFS(node, end, adj, visited)

    def solve(self, A, B):

        # start = 1
        # end = A
        # #adj = {}

        # if len(B) is 1:
        #     return 1

        # adj = defaultdict(list)
        # # for i in B:
        # #     if i[0] in adj:
        # #         adj[i[0]].append(i[1])
        # #     else:
        # #         adj[i[0]] = []
        # #         adj[i[0]].append(i[1])
        # for i in B:
        #     print(i)
        #     if(len(i) == 2):
        #         adj[i[0]].append(i[1])
        # # implement DFS
        # print(adj)

        # visited = set([])

        # return 1 if self.DFS(start, end, adj, visited) else 0

        # Use stack method
        visited = [False] * (A + 1)
        g = [[] for i in range(A + 1)]
        for i in B:
            u = i[0]
            v = i[1]
            g[u].append(v)

        q = []
        q.append(1)
        visited[1] = True
        while len(q):
            temp = q.pop(0)
            if temp == A:
                return 1
            for adj in g[temp]:
                if not visited[adj]:
                    q.append(adj)
                    visited[adj] = True
        return 0





