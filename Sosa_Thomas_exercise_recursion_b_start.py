import math
import numpy as np

def reverse(L):
    if len(L) == 0: 
        return []
    
    return [L[-1]] + reverse(L[:-1]) 

def is_sorted(L):
    if len(L) <= 1:
        return True
    
    elif L[0] > L[1]:
        return False
    
    return is_sorted(L[1:])

def print_binary(string_so_far,digits_left):
    if digits_left == 0:
        print(string_so_far)
    else:
        print_binary(string_so_far + '0', digits_left - 1)
        print_binary(string_so_far + '1', digits_left - 1)
        
def combinations(comb_so_far, list_of_lists):
    return





if __name__ == "__main__":  
    L = [4,1,7,9,3,0,6,5,2,8]
    print('Question 1')
    print(reverse(L))
    print(reverse(L[:5]))
    print(reverse(L[5:]))
    print(reverse(L[:-2]))
    print(reverse(L[4:5]))
    print(reverse(L[5:5]))
    
    print('Question 2')
    print(is_sorted(L))
    print(is_sorted([10,20,45,77]))
    print(is_sorted([]))
    print(is_sorted([2302]))
    print(is_sorted([10,20,45,77,65]))
    
    print('Question 3')
    print_binary('',2)
    print_binary('',3)
    
    print('Question 4')
    combinations([],[['salad', 'soup', 'pasta'],['steak', 'fish','lasagna'], ['cake', 'ice cream']])
    combinations([],[['Dodgers', 'Braves', 'Mets','Padres'],['Yankees', 'Astros','Red Sox','Blue Jays']])

'''
Program Output
Question 1
[8, 2, 5, 6, 0, 3, 9, 7, 1, 4]
[3, 9, 7, 1, 4]
[8, 2, 5, 6, 0]
[5, 6, 0, 3, 9, 7, 1, 4]
[3]
[]
Question 2
False
True
True
True
False
Question 3
00
01
10
11
000
001
010
011
100
101
110
111
Question 4
salad steak cake 
salad steak ice cream 
salad fish cake 
salad fish ice cream 
salad lasagna cake 
salad lasagna ice cream 
soup steak cake 
soup steak ice cream 
soup fish cake 
soup fish ice cream 
soup lasagna cake 
soup lasagna ice cream 
pasta steak cake 
pasta steak ice cream 
pasta fish cake 
pasta fish ice cream 
pasta lasagna cake 
pasta lasagna ice cream 
Dodgers Yankees 
Dodgers Astros 
Dodgers Red Sox 
Dodgers Blue Jays 
Braves Yankees 
Braves Astros 
Braves Red Sox 
Braves Blue Jays 
Mets Yankees 
Mets Astros 
Mets Red Sox 
Mets Blue Jays 
Padres Yankees 
Padres Astros 
Padres Red Sox 
Padres Blue Jays 
'''