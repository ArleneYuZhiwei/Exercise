def find(self,initial,i):
    if initial[i]==-1:
        return i
    return self. find(initial,initial[i])
def union(self,initial,a,b):
    rootA=self.find(initial, a)
    rootB = self.find(initial, b)
    if rootA != rootB:
        initial[rootA] = rootB
def findCircleNum(self, M: List[List[int]]) -> int:
    initial=[-1]*len(M)
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j]==1 and i!=j:
                self.union(initial,i,j)
return sum([x==-1 if x in intial])