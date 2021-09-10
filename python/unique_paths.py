#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10-09-2021 18:40
# @Author  : Tushar Gupta
# Leetcode: https://leetcode.com/problems/unique-paths/
import numpy as np


class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 1 or n==1:
            return 1
        dp = np.zeros((m, n), dtype='int')

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1]
                if j == 0 and i != 0:
                    dp[i][j] = dp[i - 1][j]
                if i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return int(dp[m - 1][n - 1])


if __name__ == '__main__':
    s = Solution()
    s.uniquePaths(3,7)