#a few constrains
class Solution:
    def longestMountain(self,A):
        if len(A)<2:
            return 0
        pre=[]
        aft=[]
        res=0
        sta=0
        idx=-1
        inc=True
        while idx<len(A)-2:
            idx+=1
            if A[idx]==A[idx+1]:           
                if inc:
                    pre=[]
                    sta=idx+1
                    continue
                if not inc:
                    aft=A[sta+1:idx+1]
                    if res<len(pre)+len(aft):
                        res=len(pre)+len(aft) 
                    sta=idx+1         

            if A[idx]>A[idx+1] and inc and idx==sta:
                sta=idx+1
            elif A[idx]>A[idx+1] and inc:
                pre=A[sta:idx+1]
                sta=idx
                inc=False
                if idx==len(A)-2:
                    if res<len(pre)+1:
                        return len(pre)+1
                    return res
            elif A[idx]>A[idx+1] and not inc and idx==len(A)-2:
                aft=A[sta+1:]
                if res<len(pre)+len(aft):
                    res=len(pre)+len(aft)
                return res
            elif A[idx]<A[idx+1] and not inc:
                aft=A[sta+1:idx+1]
                if res<len(pre)+len(aft):
                    res=len(pre)+len(aft)    
                pre=[]
                aft=[]
                sta=idx
                inc=True
        return res
#nested while-loop
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        lmt,res=len(A),0
        idx=0
        while idx<lmt-1:
            flag,inc=0,0
            while idx<lmt-1 and A[idx]<A[idx+1]:
                inc+=1
                if flag==0:
                    flag+=1
                idx+=1
            while idx<lmt-1 and A[idx]>A[idx+1]:
                inc+=1
                if flag==1:
                    flag+=1
                idx+=1
            while idx<lmt-1 and A[idx]==A[idx+1]:
                idx+=1
            if flag==2 and inc>=2:
                res=max(res,inc+1)
        return res 
#only consider the possible ones
class Solution:
    def longestMountain(self, A):
        res = 0
        for i in range(1, len(A) - 1):
            if A[i + 1] < A[i] > A[i - 1]:
                l = r = i
                while l and A[l] > A[l - 1]: l -= 1
                while r < len(A)-1 and A[r] > A[r + 1]: r += 1
                if r - l + 1 > res: res = r - l + 1
        return res    
                
                