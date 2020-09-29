#Student: Sosa, Thomas
# Course: CS 2302 Data Structures
#Date of last modification: September 17
# Assignment: Lab 1 Recursion
# TA: Anindita Nath
# Professor: Olac Fuentes
# Purpose: The purpose of this lab is to understand recursion uses stack to work

import numpy as np
import matplotlib.pyplot as plt
import math
import time

def subsetsum(S,g):
    if g ==0: # The empty subset adds up to 0, return True
        return True
    
    if len(S)==0 or g<0 or sum(S)<g:
        return False
    
    if subsetsum(S[1:],g-S[0]): # Take S[0]
        return True
    
    return subsetsum(S[1:],g) # Don't take S[0]

print(subsetsum([1,3,4,6,7,9],7))



def draw_squares(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=1.0,color='b') # Draw rectangle
        i1 = [1,2,3,0,1]
        q = p*(1-w) + p[i1]*w
        draw_squares(ax,n-1,q,w)
           
def draw_squares_stack(ax,n,p,w):
    S = [[n, p, w]]
    
    while len(S)>0:
        n, p, w = S.pop()
        if n>0:
            ax.plot(p[:,0],p[:,1],linewidth=1.0,color='b')
            i1 = [1,2,3,0,1]
            q = p*(1-w) + p[i1]*w
            S.append([n-1, q, w])
        
        
        
        
def circle(center,rad):
    # Returns the coordinates of the points in a circle given center and radius
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_four_circles(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=1.0,color='b')
        draw_four_circles(ax,n-1,[center[0],center[1]+radius],radius/2)
        draw_four_circles(ax,n-1,[center[0],center[1]-radius],radius/2)
        draw_four_circles(ax,n-1,[center[0]+radius,center[1]],radius/2)
        draw_four_circles(ax,n-1,[center[0]-radius,center[1]],radius/2)
        
def draw_four_circles_stack(ax,n,center,radius):
    S = [[n, center, radius]]
    
    while len(S)>0:
        n, center, radius = S.pop()
        if n>0:
            x,y = circle(center, radius)
            ax.plot(x,y,linewidth=1.0,color='b')
            S.append([n-1, [center[0],center[1]+radius], radius/2])
            S.append([n-1, [center[0],center[1]-radius], radius/2])
            S.append([n-1, [center[0]+radius,center[1]], radius/2])
            S.append([n-1, [center[0]-radius,center[1]], radius/2])
            
            
            
            

def draw_tree(ax,n,x0,y0,dx,dy):
    if n>0:
        x = [x0-dx,x0,x0+dx]
        y = [y0-dy,y0,y0-dy]
        ax.plot(x,y,linewidth=1.0,color='b')
        draw_tree(ax,n-1,x0-dx,y0-dy,dx/2,dy)
        draw_tree(ax,n-1,x0+dx,y0-dy,dx/2,dy)
        
def draw_tree_stack(ax,n,x0,y0,dx,dy):
    S = [[n,x0,y0,dx,dy]]
    
    while len(S)>0:
        n, x0, y0, dx, dy = S.pop()
        if n>0:
            x = [x0-dx,x0,x0+dx]
            y = [y0-dy,y0,y0-dy]
            ax.plot(x,y,linewidth=1.0,color='b')
            S.append([n-1, x0-dx, y0-dy, dx/2, dy])   
            S.append([n-1, x0+dx, y0-dy, dx/2, dy])   
        
        
        

def draw_four_squares(ax,n,center,size):
    if n>0:
        x = center[0] + np.array([-size,-size,size,size,-size])
        y = center[1] + np.array([-size,size,size,-size,-size])
        ax.plot(x,y,linewidth=1.0,color='b')
        for i in range(4):
            draw_four_squares(ax,n-1,[x[i],y[i]],size/2)
            
def draw_four_squares_stack(ax,n,center,size):
    S = [[n, center, size]]
    
    while len(S)>0:
        n, center, size = S.pop()
        if n>0:
            x = center[0] + np.array([-size,-size,size,size,-size])
            y = center[1] + np.array([-size,size,size,-size,-size])
            ax.plot(x,y,linewidth=1.0,color='b')
            for i in range(4):
                S.append([n-1, [x[i],y[i]], size/2])   
            
            
            
            

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    plt.show()

if __name__ == "__main__":

    plt.close("all") # Close all figures
    orig_size = 1000.0
    p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
    
    fig, ax = plt.subplots()
    start = time.time()
    draw_squares(ax,6,p,.1)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build squares1 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('squares1.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_squares(ax,10,p,.2)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recusion = end-start
    print('time to build squares2 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('squares2.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_squares(ax,5,p,.3)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build squares3 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('squares3.png')
    
    fig, ax = plt.subplots()
    start = time.time()
    draw_squares_stack(ax,6,p,.1)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build squares1 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('squares1_stack.png')
    
    fig, ax = plt.subplots()
    start = time.time()
    draw_squares_stack(ax,10,p,.2)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build squares2 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('squares2_stack.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_squares_stack(ax,5,p,.3)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build squares3 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('squares3_stack.png')
    
    
    
    

    fig, ax = plt.subplots()
    start = time.time()
    draw_four_circles(ax, 2, [0,0], 100)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build four circles1 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('four_circles1.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_four_circles(ax, 3, [0,0], 100)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build four circles2 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('four_circles2.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_four_circles(ax, 4, [0,0], 100)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build four circles3 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('four_circles3.png')
    
    fig, ax = plt.subplots()
    start = time.time()
    draw_four_circles_stack(ax, 2, [0,0], 100)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build four circles1 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('four_circles1_stack.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_four_circles_stack(ax, 3, [0,0], 100)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build four circles2 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('four_circles2_stack.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_four_circles_stack(ax, 4, [0,0], 100)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build four circles3 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('four_circles3_stack.png')    
    
    
    
    

    fig, ax = plt.subplots()
    start = time.time()
    draw_tree(ax, 4, 0, 0, 500,200)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build tree1 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('tree1.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_tree(ax, 5, 0, 0, 500,200)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build tree2 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('tree2.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_tree(ax, 6, 0, 0, 500,200)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build tree3 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('tree3.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_tree_stack(ax, 4, 0, 0, 500,200)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build tree1 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('tree1_stack.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_tree_stack(ax, 5, 0, 0, 500,200)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build tree2 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('tree2_stack.png')

    fig, ax = plt.subplots()
    start = time.time()
    draw_tree_stack(ax, 6, 0, 0, 500,200)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build tree3 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('tree3_stack.png')    
    
    
    
    
    fig, ax = plt.subplots()
    start = time.time()
    draw_four_squares(ax, 2, [0, 0], 1000)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build four squares1 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('four_squares1.png')
    
    fig, ax = plt.subplots()
    start = time.time()
    draw_four_squares(ax, 3, [0, 0], 1000)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build four squares2 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('four_squares2.png')
    
    fig, ax = plt.subplots()
    start = time.time()
    draw_four_squares(ax, 4, [0, 0], 1000)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_recursion = end-start
    print('time to build four squares3 using recursion: {:5.3f} seconds'.format(time_recursion))
    fig.savefig('four_squares3.png')
    
    fig, ax = plt.subplots()
    start = time.time()
    draw_four_squares_stack(ax, 2, [0, 0], 1000)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build four squares1 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('four_squares_stack1.png')
    
    fig, ax = plt.subplots()
    start = time.time()
    draw_four_squares_stack(ax, 3, [0, 0], 1000)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build four squares2 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('four_squares_stack2.png')
    
    fig, ax = plt.subplots()
    start = time.time()
    draw_four_squares_stack(ax, 4, [0, 0], 1000)
    end = time.time()
    set_drawing_parameters_and_show(ax)
    time_stack = end-start
    print('time to build four squares3 using stack: {:5.3f} seconds'.format(time_stack))
    fig.savefig('four_squares_stack3.png')
    
    
    