#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 29-11-2021 18:18
# @Author  : Tushar Gupta
# Leetcode : https://leetcode.com/problems/accounts-merge/ (DFS, connected components)
from collections import defaultdict


class Solution(object):

    def dfs(self, node, visited, adj, comps):

        if node in visited:
            return
        if len(adj[node]) == 0:
            visited.add(node)
            comps.append(node)
            return

        visited.add(node)
        comps.append(node)

        for child in adj[node]:
            if child not in visited:
                # comps.append(child)
                self.dfs(child, visited, adj, comps)

        return

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        adj = defaultdict(set)

        for account in accounts:

            name = account[0]
            emails = account[1:]

            # print(emails)
            node = emails[0]

            if len(emails) == 1:
                adj[node] = []
            for i in range(1, len(emails)):
                adj[node].add(emails[i])
                adj[emails[i]].add(node)

        # Do DFS for connected components for each account

        # print(adj)
        accounts_merged = []

        visited = set([])
        for account in accounts:
            name = account[0]

            start = account[1]
            # print(name)
            comps = []
            self.dfs(start, visited, adj, comps)
            # print(comps)

            if (len(comps) == 0):
                continue
            comps = sorted(comps)
            comps.insert(0, name)

            accounts_merged.append(comps)

        # print(accounts_merged)

        return accounts_merged