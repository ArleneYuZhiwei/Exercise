
def largestPerimeter(A):
    if len(A)<3:
        return 0
    A=sorted(A,reverse=True)
    print (A)
    idx=0
    while(idx<=len(A)-3):
        if A[idx+2]+A[idx+1]<=A[idx]:
            idx+=1
            continue
        else:
            return A[idx]+A[idx+1]+A[idx+2]
    return 0
