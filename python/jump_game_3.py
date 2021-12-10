#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 09-12-2021 21:43
# @Author  : Tushar Gupta
# Leetcode: Jump game
class Solution(object):
    def dfs(self, arr, idx):

        # print(idx, arr[idx])
        # arr[idx] = -1
        if arr[idx] == -1:
            return False

        r = idx + arr[idx]
        l = idx - arr[idx]

        if arr[idx] == 0:
            return True
        arr[idx] = -1
        ans_l = False
        ans_r = False

        if (l >= 0):
            ans_l = self.dfs(arr, l)

        if (r < len(arr)):
            ans_r = self.dfs(arr, r)

        return (ans_l or ans_r)

    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """

        return self.dfs(arr, start)