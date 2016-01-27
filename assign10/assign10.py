
#Brute Force Inversion Counting
def brute_count(A):
    count=0
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if A[i]>A[j]:
                count+=1
    return count


#Mergesort_and_count helper function:
def merge_and_count(L,R):
    result=[]
    count=0
    while len(L)>0 and len(R)>0:
        if L[0]<=R[0]:
            result.append(L[0])
            L=L[1:]
        else:
            result.append(R[0])
            R=R[1:]
            count+=len(L)
    while len(L)>0:
        result.append(L[0])
        L=L[1:]
    while len(R)>0:
        result.append(R[0])
        R=R[1:]
    return (result,count)


#Mergesort function
#It also counts for inversions
def mergesort_and_count(A):
    if len(A)<=1:
        return (A,0)
    else:
        middle=len(A)//2
        left = A[:middle]
        right= A[middle:]
        
        left_count=0
        right_count=0
        split_count=0
        
        (left,left_count)   = mergesort_and_count(left)
        (right,right_count) = mergesort_and_count(right)
        (result,split_count)= merge_and_count(left,right)
        total_count = left_count + right_count + split_count         
        return (result,total_count)




