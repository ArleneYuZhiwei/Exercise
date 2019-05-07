#Counter
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        items=A.split(' ')+B.split(' ')
        dict_res=Counter(items)
        return [a[0] for a in dict_res.items() if a[1]==1]
        