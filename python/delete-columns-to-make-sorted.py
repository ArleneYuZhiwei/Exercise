def minDeletionSize(A):
    times=0
    using=[k[0] for k in A]
    print (len(A),len(A[0]))
    print(len(using))
    for i in range(0,len(A[0])):
        cnt=0 
        for j in range(len(A)-1):
            if using[j]+A[j][i]>using[j+1]+A[j+1][i]:
                times+=1
                break
            else:
                cnt+=1
        if cnt==len(A)-1:
            for  j in range(len(A)):
                using[j]=using[j]+A[j][i]             
        
    return times


time=minDeletionSize(["xc","yb","za"])
print (time)