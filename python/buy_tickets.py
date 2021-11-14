#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 13-11-2021 23:13
# @Author  : Tushar Gupta
# Leetcode: 2073. Time Needed to Buy Tickets

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """

        if (len(tickets) == 1):
            return tickets[0]

        # ans = sum([i>0 for i in tickets])
        ans = 0
        while (tickets[k] > 0):

            if (tickets[k] == 0):
                break
            if (tickets[k] == 1):
                non_zero_el = sum([i > 0 for i in tickets[:k]]) + 1
                ans += non_zero_el
                break
            else:
                non_zero_el = sum([i > 0 for i in tickets])
                ans += non_zero_el
                tickets = [i - 1 for i in tickets]

        return ans

