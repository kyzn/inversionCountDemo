#Count inversions by brute force
def count_brute(A):    
    count = 0    
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if (A[i]>A[j]):
                count+=1
    return count

