def findDuplicates(nums) :
    candidates=set()
    res=[]
    for i in nums:
        if i not in candidates:
            candidates.add(i)          
        else:
            res.append(i)
    return sorted(res)
        
###
without extra space
class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for i in nums:
            if nums[abs[i]-1] < 0:
                res.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return res