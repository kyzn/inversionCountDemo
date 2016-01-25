#Count inversions by brute force
def count_brute(A):    
    count = 0    
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if (A[i]>A[j]):
                count+=1
    return count

#An example run of mergesort
#[1,3,5,2,4,6] (3 inv)
#
#Left      Right
#[1,3,5]   [2,4,6]
#       |
#               |
#Apply mergesort!
#
#[1,2,3,4,5]
#(3,2) and (5,2) 
#(5,4)








