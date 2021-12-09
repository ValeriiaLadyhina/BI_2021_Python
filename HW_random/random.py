import numpy as np
import random as rd
import time
import matplotlib.pyplot as plt

# TASK 1
def np_vs_rd():
    x = []
    y_np = []
    y_rd = []
    for number in range(0,5000):
        x.append(number)
        tic = time.time()
        np.random.uniform(0,1, size = number)
        toc = time.time()
        y_np.append(toc-tic)
        tic = time.time()
        rd.sample(range(0, 5000), number)
        toc = time.time()
        y_rd.append(toc-tic)
    plt.figure(figsize = (30,10))
    plt.plot(x,y_np, 'r', linewidth = 0.7, alpha = 0.7)
    plt.plot(x,y_rd, 'c', linewidth = 0.7)
    plt.title('Comparison of time neede for creation of list of random numbers using packages numpy and random', fontsize = 30)
    plt.legend(['numpy','random'], fontsize = 20)
    plt.grid()
    plt.xlabel('Size of needed list with random numbers', fontsize = 20)
    plt.ylabel('Time needed for creating needed size list of random numbers', fontsize = 20)



# TASK 2


# TASK 3
def randwalk(n=1000):
    x = 0
    y = 0
    step_x = [x]
    step_y = [y]
    for i in range(1,n+1):
        move = rd.randint(0,3)
        if move == 0:
            x += np.random.uniform(0,10)
        if move == 1:
            x -= np.random.uniform(0,10)
        if move == 2:
            y += np.random.uniform(0,10)
        if move == 3:
            y -= np.random.uniform(0,10)
        step_x.append(x)
        step_y.append(y)
    plt.figure(figsize=(30,30))
    plt.scatter(0,0, s=1000, c = 'green')
    plt.scatter(step_x[-1],step_y[-1], s=1000, c = 'r')
    plt.scatter(step_x, step_y, s=100, c = 'yellow')
    plt.plot(step_x, step_y, 'black')
    plt.legend(['PATH','START','END'], fontsize = 25)
    plt.title('Random walk',fontsize = 30)


# TASK 4
def sierpinski_triangle():
    A = [np.random.uniform(-10,10),np.random.uniform(-10,10)]
    B = [np.random.uniform(-10,10),np.random.uniform(-10,10)]
    C = [np.random.uniform(-10,10),np.random.uniform(-10,10)]
    start = [np.random.uniform(-10,10),np.random.uniform(-10,10)]
    plt.figure(figsize=(30,30))
    plt.scatter(A[0],A[1],c='r')
    plt.scatter(B[0],B[1],c='r')
    plt.scatter(C[0],C[1],c='r')
    plt.scatter(start[0],start[1],c='b',s=150)
    for i in range(2500):
        x = rd.randint(1,3)
        if x == 1:
            start = [(start[0]+A[0])/2, (start[1]+A[1])/2]
        elif x == 2:
            start = [(start[0]+B[0])/2, (start[1]+B[1])/2]
        else:
            start = [(start[0]+C[0])/2, (start[1]+C[1])/2]
        plt.scatter(start[0],start[1],c='b',s=5)
    plt.title('Sierpinski triangle')
    plt.legend(['A','B','C','Start'], fontsize = 20)


# TASK 5
def shuffling():
    text = input('Text to shuffle\n\n')
    pattern = r'(\b\w)(\w+)(\w\b)'
    def shuffle(word):
        beginning,to_change,end = word.groups()
        to_change = list(to_change)
        rd.shuffle(to_change)
        return beginning+''.join(to_change)+end

    print(re.sub(pattern,shuffle,text))