
#Brute Force Inversion Counting
def brute_count(A):
    count=0
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if A[i]>A[j]:
                count+=1
    return count


#Mergesort helper function:
def merge(L,R):
    result=[]
    while len(L)>0 and len(R)>0:
        if L[0]<=R[0]:
            result.append(L[0])
            L=L[1:]
        else:
            result.append(R[0])
            R=R[1:]
    while len(L)>0:
        result.append(L[0])
        L=L[1:]
    while len(R)>0:
        result.append(R[0])
        R=R[1:]
    return result


#Mergesort function
def mergesort(A):
    if len(A)<=1:
        return A
    else:
        middle=len(A)//2
        left = A[:middle]
        right= A[middle:]
        left = mergesort(left)
        right= mergesort(right)
        result= merge(left,right)
        return result
