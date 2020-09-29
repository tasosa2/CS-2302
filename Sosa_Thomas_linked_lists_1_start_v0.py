import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def first(L):
    if L.head == None:
        return -math.inf
    
    return L.head.data

def last(L):
    if L.tail == None:
        return -math.inf
    
    return L.tail.data

def swap_first_and_last(L):
    temp = 0
    
    if L.head != None:
        temp = L.head.data
        L.head.data = L.tail.data
        L.tail.data = temp

def length(t):
    t = t.head
    count = 0
    
    while t != None:
        count +=1
        t=t.next
    return count
    
def sum_list(t):
    t = t.head
    sum_l = 0
    
    while t != None:
        sum_l += t.data
        t=t.next
        
    return sum_l
    
if __name__ == "__main__":
    plt.close('all')
    L1 = sll.List()
    L1.print()
    L1.draw()
   
    L2 = sll.List()
    L2.extend([3,6,1,0,9,7,4,8,5])
    L2.print()
    L2.draw()
    
    L3 = sll.List()
    L3.append(2)
    L3.print()
    L3.draw()
    
    print('Question 1')
    print(first(L1))   
    print(first(L2))   
    print(first(L3))   
    
    print('Question 2')
    print(last(L1))   
    print(last(L2))    
    print(last(L3))    
    
    print('Question 3')   
    swap_first_and_last(L1)
    L1.print()             
    swap_first_and_last(L2) 
    L2.print()          
    swap_first_and_last(L3) 
    L3.print()  
    
    L1 = sll.List()
    L2 = sll.List()
    L2.extend([3,6,1,0,9,7,4,8,5])

    L3 = sll.List()
    L3.append(2)
   
    print('Question 4')   
    print(length(L1))
    print(length(L2))
    print(length(L3))
    
    print('Question 5')  
    print(sum_list(L1))
    print(sum_list(L2))
    print(sum_list(L3))
    
   
    

'''
[]
[3, 6, 1, 0, 9, 7, 4, 8, 5]
[2]
Question 1
-inf
3
2
Question 2
-inf
5
2
Question 3
[]
[5, 6, 1, 0, 9, 7, 4, 8, 3]
[2]
Question 4
0
9
1
Question 5
0
43
2
'''