#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 29-08-2021 01:58
# @Author  : Tushar Gupta
# Leetcode Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        max_so_far = 0
        curr_max = 0
        for i in range(len(prices) - 1, 0, -1):
            if prices[i] > max_so_far:
                max_so_far = prices[i]
            curr_max = -prices[i - 1] + max_so_far if -prices[i - 1] + max_so_far > curr_max else curr_max
        return curr_max


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([3, 4, 6, 7, 8]))
