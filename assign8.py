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

#Mergesort function
def mergesort(A):
    if len(A)<=1:
        return A
    else:
        mid=len(A)//2
        left  = A[:mid]
        right = A[mid:]
        
        left  = mergesort(left)
        right = mergesort(right)        
        result= merge(left,right)
        
        return result
        
#merge function to help mergesort
def merge(L,R):
    result=[]
    while len(L)>0 and len(R)>0:
        if(L[0]<=R[0]):
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
    
        











