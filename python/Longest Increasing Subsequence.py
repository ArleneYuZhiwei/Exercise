# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:36:13 2018

@author: 11
"""
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """  
    def flag(sub,new):
        l,h=0,len(sub)-1
        while (l<=h):
            m=(h+l)//2
            if sub[m]<new:
                l=m+1
            elif new<sub[m]:
                h=m-1
            else:
                return m
        return l
    sub=[]
    for new in nums:
        f=flag(sub,new)
        if f== len(sub):
            sub.append(new)
        else:
            sub[f]=new
    return len(sub)
print (lengthOfLIS([10,9,2,5,3,7,101,18]))
            
print ((0+1)//2  )      
        
  