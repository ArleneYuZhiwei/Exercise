# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:53:21 2018

@author: 11
"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        def number(ln):
            sum_tmp=0
            offset=1
            while ln :
                sum_tmp += ln.val * offset
                offset *= 10
                ln = ln.next
            return sum_tmp
        total = list(str(number(l1)+number(l2)))
        return [ int(a) for a in total[::-1] ]
