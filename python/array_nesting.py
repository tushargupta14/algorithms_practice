#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 03-09-2021 16:49
# @Author  : Tushar Gupta
# Leetcode: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3960/
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hmap = defaultdict(int)

        if (len(nums) == 1):
            return 1
        curr = 0
        idx_pointer = 0
        num_len = len(nums)
        largest = 0
        while (idx_pointer < num_len):
            if (nums[idx_pointer] == -1):
                idx_pointer += 1
            else:
                num_set = set()
                curr = idx_pointer
                while (curr not in num_set):
                    num_set.add(curr)
                    temp = nums[curr]
                    nums[curr] = -1
                    curr = temp

                if len(num_set) > largest:
                    largest = len(num_set)

        return largest