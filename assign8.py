import numpy as np
import scipy
from matplotlib import pyplot as plt
import timeit

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
def mergesort_and_count(A):
    if len(A)<=1:
        return (A,0)
    else:
        mid=len(A)//2
        
        leftcounter=0        
        rightcounter=0
        splitcounter=0        
        
        left  = A[:mid]
        right = A[mid:]
        
        (left,leftcounter) = mergesort_and_count(left)
        (right,rightcounter) = mergesort_and_count(right)        
        (result,splitcounter)= merge_and_count(left,right)
        
        totalcounter = leftcounter+rightcounter+splitcounter        
        
        return (result, totalcounter)
        
#merge function to help mergesort
def merge_and_count(L,R):
    result=[]
    counter=0
    while len(L)>0 and len(R)>0:
        if(L[0]<=R[0]):
            result.append(L[0])
            L=L[1:]
        else: #count inversions too
            result.append(R[0])
            R=R[1:]
            counter+=len(L)
    
    while len(L)>0:
        result.append(L[0])
        L=L[1:]
            
    while len(R)>0:
        result.append(R[0])
        R=R[1:]
            
    return (result,counter)
    
    


#TIMING AND PLOTTING
brute_results=[]
merge_results=[]

size_of_input = range(0,1000,10)

for a in size_of_input:
    A = np.arange(a)
    A = np.random.permutation(A)    
    t1 = timeit.Timer(lambda: count_brute(A))
    t2 = timeit.Timer(lambda: mergesort_and_count(A))
    
    brute_result = t1.repeat(repeat=3,number=1)
    brute_result = scipy.mean(brute_result)
    brute_results.append(brute_result)
    
    merge_result = t2.repeat(repeat=3,number=1)
    merge_result = scipy.mean(merge_result)
    merge_results.append(merge_result)
    

plt.figure()
plt.plot(size_of_input,brute_results,label="Brute Force")
plt.plot(size_of_input,merge_results,label="Mergesort")
plt.legend()

plt.xlabel("Size of input")
plt.ylabel("Time (s)")
plt.title("Counting Number of Inversions")
plt.show()