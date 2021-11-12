#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11-11-2021 20:02
# @Author  : Tushar Gupta
# Problem : https://leetcode.com/explore/featured/card/graph/619/depth-first-search-in-graph/3849/

class Solution(object):

    def dfs(self, source, graph, visited, path_stack, res):

        neighs = graph[source]
        if (len(neighs) == 0):
            return
        curr_path = path_stack.pop()

        for node in neighs:
            if node == self.target:
                temp = curr_path + [node]
                res.append(temp)

            elif visited[node] == 0:
                # start visiting
                visited[node] = -1
                temp = curr_path + [node]
                path_stack.append(temp)
                self.dfs(node, graph, visited, path_stack, res)
                visited[node] = 0

        return

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        dest = len(graph) - 1

        self.target = dest

        visited = [0] * len(graph)

        path_stack = [[0]]

        visited[0] = -1

        res = []
        self.dfs(0, graph, visited, path_stack, res)
        visited[0] = 1

        return res