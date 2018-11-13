# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:17:14 2018

@author: 11
"""
#Time Limit Exceeded
#class Solution:
#    def maxSubArray(self, nums):
#        if len(nums)==0:
#            return 0
#        sumlist=[]
#        sumlist.append(nums[0])
#        for i in range(1,len(nums)):
#            a=nums[i]
#            templist=[]
#            templist.append(a)
#            for j in range(i-1,-1,-1):
#                a+=nums[j]
#                templist.append(a)
#            sumlist.append(max(templist))
#        return max(sumlist)

#def  maxSubArray(nums):
#    """
#    :type nums: List[int]
#    :rtype: int
#    """   
#    if len(nums)==0:
#        return 0
#    res=nums[0]
#    for i in range(0,len(nums)):
#        summation=nums[i]
#        if summation>res:
#            res=summation
#        for j in range(i+1,len(nums)):
#            summation+=nums[j]
#            if summation>res:
#                res=summation            
#    return res
                
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        vector<int>s(nums.size(),0);
        vector<int>p(nums.size(),0);
        s[0] = nums[0];
        p[0] = nums[0];
        for(int i = 1;i<nums.size();++i){
            p[i] = max(p[i-1]+nums[i],nums[i]);
            s[i] = max(s[i-1],p[i]);
        }
        return s[nums.size()-1];
        
    }
};
