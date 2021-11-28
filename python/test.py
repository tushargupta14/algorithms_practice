#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 14-11-2021 20:02
# @Author  : Tushar Gupta

def solution(A, B, C, D):
    # write your code in Python 3.6

    nums = [str(A), str(B), str(C), str(D)]
    # ans = 0
    # curr_str = ''
    # ans = recurse_stack(curr_str, nums, [-1])

    ans = 0
    for i in nums:
        lev_1 = nums.copy()
        lev_1.remove(i)

        for j in lev_1:
            lev_2 = lev_1
            lev_2.remove(j)

            for k in lev_2:
                lev_3 = lev_2
                lev_3.remove(k)

                for l in lev_3:
                    lev_4 = lev_3
                    lev_4.remove(l)

                    num = i + j + k + l
                    print(num)
                    if len(num) == 4 and int(num) <= 2359:
                        ans += 1

    return ans
