#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 01-12-2021 19:56
# @Author  : Tushar Gupta
# Leetcode: House robber
class Solution(object):

    # self.max_val = 0
    def recurse(self, arr, idx, curr_sum):

        # print("idx", idx)

        n = len(arr)

        if (idx >= n):
            return 0

        if (idx in [n - 2, n - 1]):
            return curr_sum + arr[idx]
        curr_sum += arr[idx]

        # print("curr_sum", curr_sum)

        tot = max(self.recurse(arr, idx + 2, curr_sum), self.recurse(arr, idx + 3, curr_sum))

        # print(tot)

        return tot

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # val = max(self.recurse(nums, 0, 0), self.recurse(nums, 1, 0))

        n = len(nums)
        dp = [0] * len(nums)

        if (n == 1):
            return nums[0]
        if (n == 2):
            return max(nums)

        dp[n - 1] = nums[n - 1]
        dp[n - 2] = nums[n - 2]
        dp[n - 3] = nums[n - 1] + nums[n - 3]

        i = n - 4

        while (i >= 0):
            dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
            i -= 1

        return max(dp[0], dp[1])

        return val
