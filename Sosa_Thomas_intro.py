# Introduction to Python exercise
# Rename this file to lastname_firstname_intro.py before submitting
import numpy as np
import math

def divisible(a,b):
    
    if a % b == 0:
        return True
    
    else:
        return False
    
def reverse(s):
    rev =''
    
    rev = s[::-1] # using slicing
    '''
    for i in s:
        rev = i + rev # using for loop
    '''
    return  rev

def remove_vowels(s):
    rv =''
    vowels = 'aeiou'
    
    for i in s:
        if i not in vowels:
            rv = rv + i
    
    return  rv

def max_array(A):
    mx = 0
    
    if len(A) == 0:
        return -math.inf
    
    for i in range(0,len(A)):
        if A[i] > mx:
            mx = A[i]
    
    return mx

def find(A,x):
    
    for i in range(0,len(A)):
        if A[i] == x:
            return i
        
    return -1
        
def is_square(A):
    
    if len(A.shape) != 2:
        return False
    
    if len(A) == len(A[0]):
        return True
    
    return False
    
def diagonal(A):
    B = np.zeros(len(A), dtype=int)
    
    for i in range(0,len(A)): 
        B[i] = A[i][i]
    
    return B
    
def sec_diagonal(A):
    B = np.zeros(len(A), dtype=int)
    
    for r in range(0,len(A)):
        B[r] = A[r][len(A)-1-r]
            
    return B

def swap_rows(A,i,j):
    A_second = A.copy()
    
    for r in range(0,len(A)):
        for c in range(0,len(A[0])):
            if r == i:
                A_second[r][c] = A[j][c]
            elif r == j:
                A_second[r][c] = A[i][c]
            else: 
                A_second[r][c] = A[r][c]
    
    return A_second

def greater_than_list(L,x):
    
    G = []
    
    for i in range(0, len(L)):
        if L[i] > x:
            G.append(L[i])
    
    return G

def split(L):
    l_even, l_odd = [],[]
    
    for i in range(0,len(L)):
        if i % 2 == 0:
            l_even.append(L[i])
        if i %2 == 1:
            l_odd.append(L[i])
            
    return l_even, l_odd

if __name__ == "__main__": # main program won't be exeuted if the program is imported
    
    print('Question 1')
    print(divisible(8,2))       
    print(divisible(8,3))       
    print(divisible(105,3))     
    print(divisible(105,9))    
    
    print('Question 2')
    print(reverse('UTEP'))
    print(reverse('A'))
    print(reverse(''))
    print(reverse('kayak'))
    print(reverse('reverse'))
    
    print('Question 3')
    print(remove_vowels('UTEP'))      
    print(remove_vowels('racecar'))     
    print(remove_vowels('Week'))        
    print(remove_vowels('miners'))      
    
    print('Question 4')
    A0 = np.array([2,5,7,1,2,5,7,8,9,0])
    A1 = np.array([2,5,7,1,2,5,7,0])
    A2 = np.array([2,5,7,11,2,5,7,8,9,0])
    A3 = np.array([2,5,3,0])
    A4 = np.array([2302])
    A5 = np.array([])
    print(max_array(A0))                  
    print(max_array(A1))                  
    print(max_array(A2))                  
    print(max_array(A3))                  
    print(max_array(A4))     
    print(max_array(A5))     
    
    print('Question 5')
    print(find(A0,5))      
    print(find(A1,0))      
    print(find(A2,4))      
    print(find(A3,2))  
    print(find(A4,5))  
    print(find(A5,5))   
    
    print('Question 6')
    A = np.arange(25).reshape((5,5))
    B = np.array([2,5,7,1,2,7,8,9,0]).reshape((3,3))
    C = np.arange(30).reshape((6,5))
    D = np.array([2,5,7,1,2,7,8,9,0,10]).reshape((2,5))
    E = np.array([2,5,7,1,2,7,8,9,0])
    F = np.arange(25).reshape((5,5,1)) 
    print(is_square(A))
    print(is_square(B))
    print(is_square(C))
    print(is_square(D))
    print(is_square(E))
    print(is_square(F))
    
    print('Question 7')
    A = np.arange(25).reshape((5,5))
    print(A)
    B = np.array([2,5,7,1,2,7,8,9,0]).reshape((3,3))
    print(B)
    print(diagonal(A))        
    print(diagonal(B))        
    
    print('Question 8')
    print(sec_diagonal(A))        
    print(sec_diagonal(B))        
    
    print('Question 9')
    A = np.arange(25).reshape((5,5))
    print(A)
    B = np.array([2,5,7,1,2,7,8,9,0,12,10,11]).reshape((3,4))
    print(B)
    print(swap_rows(A,2,4))   
    print(swap_rows(B,0,2))    
    print(A)     
    print(B)
  
    print('Question 10')
    Ls = [2,5,7,1,2,5,7,8,9,0]
    print(greater_than_list(Ls,4))  
    print(greater_than_list(Ls,9))  
    print(greater_than_list(Ls,-1))  
    print(greater_than_list(Ls,7))  
    
    print('Question 11')
    Ls = [2,5,7,1,2,5,7,8,9,0]
    print(Ls)
    Lo,Le = split(Ls)
    print(Lo)  
    print(Le)  
    print(Ls)
    
    
'''
Program Output:
Question 1
True
False
True
False
Question 2
PETU
A

kayak
esrever
Question 3
UTEP
rccr
Wk
mnrs
Question 4
9
7
11
5
2302
-inf
Question 5
1
7
-1
0
-1
-1
Question 6
True
True
False
False
False
False
Question 7
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
[[2 5 7]
 [1 2 7]
 [8 9 0]]
[ 0  6 12 18 24]
[2 2 0]
Question 8
[ 4  8 12 16 20]
[7 2 8]
Question 9
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
[[ 2  5  7  1]
 [ 2  7  8  9]
 [ 0 12 10 11]]
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [20 21 22 23 24]
 [15 16 17 18 19]
 [10 11 12 13 14]]
[[ 0 12 10 11]
 [ 2  7  8  9]
 [ 2  5  7  1]]
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
[[ 2  5  7  1]
 [ 2  7  8  9]
 [ 0 12 10 11]]
Question 10
[5, 7, 5, 7, 8, 9]
[]
[2, 5, 7, 1, 2, 5, 7, 8, 9, 0]
[8, 9]
Question 11
[2, 5, 7, 1, 2, 5, 7, 8, 9, 0]
[2, 7, 2, 7, 9]
[5, 1, 5, 8, 0]
[2, 5, 7, 1, 2, 5, 7, 8, 9, 0]
'''