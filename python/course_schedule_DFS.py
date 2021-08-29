#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 29-08-2021 02:01
# @Author  : Tushar Gupta
# Leetcode : https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.visited = defaultdict(int)
        self.cycle = 0

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def print_graph(self):
        for key in self.adj.keys():
            print(key, self.adj[key])

    def mark_visited(self, u):
        self.visited[u] = 2

    def mark_gray(self, u):
        self.visited[u] = 1

    def dfs(self, u, cycle, v_stack):

        if not self.adj[u]:
            self.mark_visited(u)
            v_stack.append(u)
            return 0

        self.mark_gray(u)
        for v in self.adj[u]:
            # print("vertex", v)
            if self.visited[v] == 0:
                self.mark_gray(v)
                cycle = self.dfs(v, cycle, v_stack)

            if self.visited[v] == 1:
                # back edge, visit gray node
                return 1

        self.mark_visited(u)
        v_stack.append(u)
        return cycle


class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if prerequisites == []:
            return [i for i in range(numCourses)]
        graph = Graph()

        cycle = 0
        for pair in prerequisites:
            graph.add_edge(pair[1], pair[0])

        v_stack = []
        for u in graph.adj.keys():
            graph.visited[u] = 0
        for u in range(numCourses):
            rec = []
            if graph.visited[u] == 0:
                cycle = graph.dfs(u, cycle, v_stack)
            if cycle == 1:
                break
        if cycle == 1:
            return []
        return v_stack[::-1]

if __name__ == "__main__":
    s = Solution()
    prereqs = [[1,0],[2,0],[3,1],[3,2]]
    print(s.findOrder(4, prereqs))