from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        cn=Counter(S)
        co=sorted(cn, key=cn.get, reverse=True)
        if cn[co[0]]>int((len(S)-1)/2)+1:
            return ""
        reorder=""
        for i in co:
            reorder+=i*cn[i]
        res=""
        if len(S)%2 ==0:
            res1=reorder[:int(len(S)/2)]
            res2=reorder[int(len(S)/2):]
            for i in range(len(res1)):
                res+=res1[i]+res2[i]
        else:
            res1=reorder[:int(len(S)/2)+1]
            res2=reorder[int(len(S)/2)+1:]
            for i in range(len(res1)-1):
                res+=res1[i]+res2[i]
            res+=res1[-1]
        return res
            