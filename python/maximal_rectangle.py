#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 30-11-2021 19:55
# @Author  : Tushar Gupta
# Leetcode: https://leetcode.com/problems/maximal-rectangle/
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if len(matrix) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        dp = [[-1 for _ in range(m)]] * n

        for i in range(n):
            if matrix[i][0] == "1":
                curr = 1
            else:
                curr = 0
            res = []
            res.append(curr)

            for j in range(1, m):
                # print(i,j)
                if matrix[i][j] == "1":
                    res.append(curr + 1)
                    curr += 1
                else:
                    res.append(0)
                    curr = 0
            dp[i] = res

            # print(dp)

        max_area = 0

        for i in range(n):

            for j in range(m):

                k = i - 1
                width = dp[i][j]
                height = 1
                max_area = max(width * height, max_area)

                # print(i,j)
                while (k >= 0 and dp[k][j] != 0):
                    width = min(dp[k][j], width)
                    if width > 0:
                        height += 1
                        # print("w,h", width, height,k,j)
                        max_area = max(width * height, max_area)
                    else:
                        # print(width, height)
                        break

                    k -= 1

        return max_area






