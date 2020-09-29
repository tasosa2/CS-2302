import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def zero2n(n): 
    L=sll.List()
    
    if n < 0:
        return L
    
    for i in range(0, n+1):
       L.append(i)
    
    return L

def appears(t,x):
    return appears_n(t.head, x)
 
def appears_n(L, num):
    if L == None:
        return False
    
    if L.data == num:
        return True
    
    return appears_n(L.next, num)
    
    
def appears_loop(L,x):
    L = L.head
    
    while L != None:
        if L.data == x:
            return True
        L = L.next
        
    return False

def insert_head(L,x):
    L.head = sll.ListNode(x,L.head)
    
    if L.tail == None:
        L.tail = L.head
    
def remove_first(L):
    if L.head != None:
        L.head = L.head.next
            
def remove_last(L):
    if L.head == None:
        return
    
    if L.head == L.tail:
        L.head = None
        L.tail = None
        return
    
    t = L.head
    
    while t.next != L.tail:
        t = t.next
    L.tail = t
    t.next = None
  
def is_sorted(t):
    if type(t) == sll.List:
        t = t.head
        
    if t == None or t.next == None:
        return True
    
    if t.data > t.next.data:
        return False
    
    return is_sorted(t.next)
    
def is_sorted_loop(L):
    L = L.head
    
    if L == None:
        return True
    
    while L.next != None:
        if L.data > L.next.data:
            return False
        L = L.next
        
    return True


if __name__ == "__main__":
    plt.close('all')
   
    print('Question 1')
    L1 = zero2n(-9)
    L1.print()
    L1 = zero2n(0)
    L1.print()
    L1 = zero2n(1)
    L1.print()
    L1 = zero2n(5)
    L1.print()
    
    print('Question 2')
    L2 = sll.List()
    L2.extend([3,6,1,4,0,9,7,4,8,5,9,7,19])
    print(appears(L2,0))
    print(appears(L2,10))
    print(appears(L2,19))
    
    print('Question 3')
    L2 = sll.List()
    L2.extend([3,6,1,4,0,9,7,4,8,5,9,7,19])
    print(appears_loop(L2,0))
    print(appears_loop(L2,10))
    print(appears_loop(L2,19))
    
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
    
    print('Question 4')   
    insert_head(L1,3)
    L1.print()
    insert_head(L2,4)
    L2.print()
    insert_head(L3,5)
    L3.print()
    insert_head(L4,1)
    L4.print()
    insert_head(L5,1)
    L5.print()
    
    
    print('Question 5')
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
    remove_first(L1)
    L1.print()
    remove_first(L2)
    L2.print()
    remove_first(L3)
    L3.print()
    remove_first(L4)
    L4.print()
    remove_first(L5)
    L5.print()
    
    print('Question 6')
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
    remove_last(L1)
    L1.print()
    remove_last(L2)
    L2.print()
    remove_last(L3)
    L3.print()
    remove_last(L4)
    L4.print()
    remove_last(L5)
    L5.print()
    
    print('Question 7')  
    L1 = sll.List()
    L2 = sll.List()
    L2.append(2)
    L3 = sll.List()
    L3.extend([3,6,1,4,0,9,7,4,8,5,9,7,9])
    L4 = sll.List()
    L4.extend([2,3,6,7,8,9])
    L5 = sll.List()
    L5.extend([2,3,6,7,8,9,0])
   
    print(is_sorted(L1))
    print(is_sorted(L2))
    print(is_sorted(L3))
    print(is_sorted(L4))
    print(is_sorted(L5))
    
    print('Question 8')  
    print(is_sorted_loop(L1))
    print(is_sorted_loop(L2))
    print(is_sorted_loop(L3))
    print(is_sorted_loop(L4))
    print(is_sorted_loop(L5))
    
'''
Question 1
[]
[0]
[0, 1]
[0, 1, 2, 3, 4, 5]
Question 2
True
False
True
Question 3
True
False
True
Question 4
[3]
[4, 2]
[5, 3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7, 9]
[1, 2, 3, 6, 7, 8, 9]
[1, 2, 3, 6, 7, 8, 9, 0]
Question 5
[]
[]
[6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7, 9]
[3, 6, 7, 8, 9]
[3, 6, 7, 8, 9, 0]
Question 6
[]
[]
[3, 6, 1, 4, 0, 9, 7, 4, 8, 5, 9, 7]
[2, 3, 6, 7, 8]
[2, 3, 6, 7, 8, 9]
Question 7
True
True
False
True
False
Question 8
True
True
False
True
False
'''