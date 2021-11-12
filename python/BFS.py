#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11-11-2021 21:51
# @Author  : Tushar Gupta
# Check if node is reachable
from collections import defaultdict
from collections import deque


class Solution(object):

    def validPath(self, n, edges, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: int
        :type end: int
        :rtype: bool
        """

        q = deque()

        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        q.append(start)

        visited = set([start])

        while (len(q) > 0):

            temp = q.popleft()
            if temp == end:
                return True

            neighs = graph[temp]
            # print neighs
            for node in neighs:
                if node not in visited:
                    visited.add(node)
                    q.append(node)

        return False
