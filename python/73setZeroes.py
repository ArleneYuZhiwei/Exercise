class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        A=matrix
        idx_i=set()
        idx_j=set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==0:
                    idx_i.add(i)
                    idx_j.add(j)

        for  i in range(len(A)):
            if i in idx_i:
                A[i]=[0 for l in range(len(A[0]))]
            else:
                for j in range(len(A[0])):
                    if j in idx_j:
                        A[i][j]=0

