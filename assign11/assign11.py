import numpy as np
import scipy
import timeit
from matplotlib import pyplot as plt

#Count inversions by brute force
def brute_count(A):
    count = 0
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if (A[i]>A[j]):
                count+=1
    return count
    

#Mergesort_count helper function
def merge_count(L,R):
    result = []
    count = 0
    
    while len(L)>0 and len(R)>0:
        if (L[0]<=R[0]):
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
    
    
    
#Mergesort
def mergesort_count(A):
    if len(A)<=1:
        return (A,0)
    else:
        mid= len(A)//2
        L = A[:mid]
        R = A[mid:]
        left_inv=0        
        right_inv=0
        split_inv=0
        
        (L,left_inv) = mergesort_count(L)
        (R,right_inv) = mergesort_count(R)
        (result,split_inv) = merge_count(L,R)

        total_inv = left_inv + right_inv + split_inv        
        
    return (result,total_inv)
        
        
#Timing
        
merge_results=[]
brute_results=[]
input_size=range(0,1000,10)

for n in input_size:
    A=np.arange(n)
    A=np.random.permutation(A)
    
    #timers
    tm=timeit.Timer(lambda: mergesort_count(A))
    tb=timeit.Timer(lambda: brute_count(A))

    #single results
    rm=scipy.mean(tm.repeat(repeat=3,number=1))
    merge_results.append(rm)
    rb=scipy.mean(tb.repeat(repeat=3,number=1))
    brute_results.append(rb)
    

#Plotting
plt.figure()

plt.plot(input_size,merge_results,label="Mergesort")
plt.plot(input_size,brute_results,label="Brute force")

plt.xlabel("Input size")
plt.ylabel("Time (s)")
plt.title("Inversion Counting Runtimes")

plt.legend()
plt.show()

        
        
    
