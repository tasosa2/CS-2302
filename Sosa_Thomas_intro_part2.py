# Introduction to Python exercise
# Rename this file to lastname_firstname.py before submitting
import numpy as np
import math 
    
def prime(n):
    
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
        
    return False

def sum_digits(n):
    sum_d = 0
    
    while n != 0:
        sum_d += n % 10
        n = n // 10
    
    return  sum_d

def pal(s):
    
    if s[:] == s[::-1]:
        return True
    
    return False

def sum_array(A):
    summation = 0
    
    for i in A:
        summation += i
    
    return summation

def replace_array(A,i,j):
    for index in range(0, len(A)):
        if A[index] == i:
            A[index] = j
    
    return A

def sec_diagonal_sum(A):
    s = 0
    B = np.zeros(len(A), dtype=int)
    
    for i in range(0,len(A)):  # I just reused sec_diagonal from the last HW.
        B[i] = A[i][len(A)-1-i] # Would write this code differently if I had
        s += B[i]               # too from scratch.
            
    return s

def diagonal(A):
    d = np.zeros(A.shape[0],dtype=type(A))
    
    for i in range(0,len(A)): 
        d[i] = A[i][i]
    
    return d

def swap_columns(A,i,j):
    A2 = A.copy()
    
    for r in range(0,len(A)):
        for c in range(0,len(A[0])):
            if c == i:               # Same as swap rows from prev HW. Just
                A2[r][c] = A[r][j]   # swapped the checks from rows to columns
            elif c == j:
                A2[r][c] = A[r][i]
            else: 
                A2[r][c] = A[r][c]
    
    return A2

def replace_max_array(A,x):
    A2 = A.copy()
    mx = 0
    
    if len(A) == 0 and len(A[0]) == 0:
        return -math.inf
    
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if A[i][j] > mx:
                mx = A[i][j]
    
    for i in range(0,len(A2)):
        for j in range(0,len(A2[0])):
            if A2[i][j] == mx:
                A2[i][j] = x
            
    return A2

def merge(L1,L2):
    L = []
    i = 0
    j = 0
    
    while True:
        if i < len(L1) and j < len(L2):
            if L1[i] < L2[j]:
                L.append(L1[i])
                i += 1
            else:
                L.append(L2[j])
                j += 1
                
        elif i == len(L1):
            for e in range(j, len(L2)):
                L.append(L2[e])
            return L
            
        elif j == len(L2):
            for e in range(i, len(L1)):
                L.append(L1[e])
            return L      
   
def split(L):
    smaller, greater_or_equal = [],[]

    if len(L) == 0:
        return smaller, greater_or_equal

    pivot = L[0]
    for i in L:
        if i < pivot:
            smaller.append(i)
        else:
            greater_or_equal.append(i)
            
    return smaller, greater_or_equal

if __name__ == "__main__":
    
    print('Question 1')
    print(prime(2))             
    print(prime(49))            
    print(prime(151))           
    print(prime(39203))         
    
    print('Question 2')
    print(sum_digits(0))            
    print(sum_digits(2))             
    print(sum_digits(49))            
    print(sum_digits(151))           
    print(sum_digits(39203))         
    
    print('Question 3')
    print(pal('UTEP'))            
    print(pal('racecar'))          
    print(pal('W'))                 
    print(pal('Week'))             
    print(pal('ABBA'))      
    print(pal(''))      
     
    print('Question 4')
    A0 = np.array([2,5,7,1,2,5,7,8,9,0])
    A1 = np.array([2,5,7,1,2,5,7,0])
    A2 = np.array([2,5,7,11,2,5,7,8,9,0])
    A3 = np.array([2,5,3,0])
    print(sum_array(A0))                 
    print(sum_array(A1))                  
    print(sum_array(A2))                 
    print(sum_array(A3))                  
    
    print('Question 5')
    A = np.array([2,5,17,1,2,5,17,8,9,0])
    print(A)                    
    replace_array(A,17,-100)
    print(A)                    
    replace_array(A,0,-1)
    print(A)                    
    replace_array(A,2,-8)
    print(A)                    
        
    print('Question 6')
    A = np.arange(25).reshape((5,5))
    B = np.array([2,5,7,1,2,7,8,9,0]).reshape((3,3))
    print(A)
    print(B)
    print(sec_diagonal_sum(A))        
    print(sec_diagonal_sum(B))     
    
    print('Question 7')
    A = np.arange(25).reshape((5,5))
    B = np.array([2,5,7,1,2,7,8,9,0]).reshape((3,3))
    print(A)
    print(B)
    print(diagonal(A))        
    print(diagonal(B))        
    
    print('Question 8')
    A = np.arange(25).reshape((5,5))
    print(A)
    B = np.array([2,5,7,1,2,7,8,9,0,12,10,11]).reshape((3,4))
    print(B)
    print(swap_columns(A,2,4))   
    print(swap_columns(B,0,2))    
    print(A)     
    print(B)
    
    print('Question 10')
    L1 = [2,5,7,12]
    L2 = [1,7,8,9,23,55]
    L3 = [2302]
    L4 = []
    
    for La in [L1,L2,L3,L4]:
        for Lb in [L1,L2,L3,L4]:
            print(merge(La,Lb))  
   
    print('Question 11')
    L1 = [6,1,10,4,2,5,7,12]
    L2 = [12,1,7,8,9,23,55]
    L3 = [2302]
    L4 = []
    
    for L in [L1,L2,L3,L4]:
        print(split(L)) 
    
'''
Program Output:     
Question 1
True
False
True
False
Question 2
0
2
13
7
17
Question 3
False
True
True
False
True
True
Question 4
46
29
56
10
Question 5
[ 2  5 17  1  2  5 17  8  9  0]
[   2    5 -100    1    2    5 -100    8    9    0]
[   2    5 -100    1    2    5 -100    8    9   -1]
[  -8    5 -100    1   -8    5 -100    8    9   -1]
Question 6
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
[[2 5 7]
 [1 2 7]
 [8 9 0]]
60
17
Question 7
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
[[2 5 7]
 [1 2 7]
 [8 9 0]]
[0 6 12 18 24]
[2 2 0]
Question 8
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
[[ 2  5  7  1]
 [ 2  7  8  9]
 [ 0 12 10 11]]
[[ 0  1  4  3  2]
 [ 5  6  9  8  7]
 [10 11 14 13 12]
 [15 16 19 18 17]
 [20 21 24 23 22]]
[[ 7  5  2  1]
 [ 8  7  2  9]
 [10 12  0 11]]
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
[[ 2  5  7  1]
 [ 2  7  8  9]
 [ 0 12 10 11]]
Question 10
[2, 2, 5, 5, 7, 7, 12, 12]
[1, 2, 5, 7, 7, 8, 9, 12, 23, 55]
[2, 5, 7, 12, 2302]
[2, 5, 7, 12]
[1, 2, 5, 7, 7, 8, 9, 12, 23, 55]
[1, 1, 7, 7, 8, 8, 9, 9, 23, 23, 55, 55]
[1, 7, 8, 9, 23, 55, 2302]
[1, 7, 8, 9, 23, 55]
[2, 5, 7, 12, 2302]
[1, 7, 8, 9, 23, 55, 2302]
[2302, 2302]
[2302]
[2, 5, 7, 12]
[1, 7, 8, 9, 23, 55]
[2302]
[]
Question 11
([1, 4, 2, 5], [6, 10, 7, 12])
([1, 7, 8, 9], [12, 23, 55])
([], [2302])
([], [])
'''    