import collections
from  collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        char_dict=collections.defaultdict(list)
        for i in A:
            tmp=Counter(i)
            for k in tmp.items():
                char_dict[k[0]].append(k[1])
        res=[]
        for k,v in char_dict.items():
            if len(v)==len(A):
                times=min(v)
                for tt in range(times):
                    res.append(k)
        return res

#an slower but easy way
#there is no need to consider chars out of the first word
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:                        
        common_counter = Counter(A[0])                
        for str in A[1:]:
            common_counter &= Counter(str)                                    
        return list(common_counter.elements())
#faster way      
#if a char do not appear in any word, it cannot be the answer
class Solution(object):
    def commonChars(self, A):       
        if len(A) == 1:
            return list(A[0])
        all_length = len(A[0])
        temp = all_length
        A0 = sorted(A[0])
        currI = ''
        result = []
        for i in A0:
            if i == currI:
                continue
            for j in range(len(A)):
                temp = min(A[j].count(i), temp)
                if temp == 0:
                    break
            result = result + list(i * temp)
            currI = i
            temp = all_length
        return result