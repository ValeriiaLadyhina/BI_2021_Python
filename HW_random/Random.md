```python
import numpy as np
import random as rd
import time
import matplotlib.pyplot as plt
import re
import pandas as pd
```

TASK 1


```python
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
```




    Text(0, 0.5, 'Time needed for creating needed size list of random numbers')




    
![png](output_2_1.png)
    


TASK 2


```python
def is_sorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            return False
    return True

def monkey_sort(list):
    while is_sorted(list) is False:
        rd.shuffle(list)        
    return list

def time_monkey_sort():
    results = dict()
    for number in range(0,11):
        result_time = []
        for i in range(5):
            list_to_sort = np.random.normal(size=number)
            tic = time.time()
            monkey_sort(list_to_sort)
            toc = time.time()
            result_time.append(toc-tic)
        results[number] = result_time
    labels, data = results.keys(), results.values()
    plt.boxplot(data)
    plt.xticks(range(1, len(labels) + 1), labels)



```


```python
time_monkey_sort()
```


    
![png](output_5_0.png)
    


TASK 3 Random walk


```python
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
    
randwalk()
```


    
![png](output_7_0.png)
    


TASK 4


```python
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
sierpinski_triangle()
```


    
![png](output_9_0.png)
    


TASK 5


```python
def shuffling():
    text = input('Text to shuffle\n\n')
    pattern = r'(\b\w)(\w+)(\w\b)'
    def shuffle(word):
        beginning,to_change,end = word.groups()
        to_change = list(to_change)
        rd.shuffle(to_change)        
        return beginning+''.join(to_change)+end

    print('\n\n', re.sub(pattern,shuffle,text))
```


```python
shuffling()
```

    Text to shuffle
    
    "По рзеузльаттам илссоевадний одонго анлигсйокго унвиертисета, не иеемт занчнеия, в каокм проякде рсапжоолены бкувы в солве. Галовне, чотбы преавя и пслонедяя бквуы блыи на мсете. осатьлыне бкувы мгоут селдовтаь в плоонм бсепордяке, все-рвано ткест чтаитсея без побрелм. Пичрионй эгото ялвятеся то, что мы не чиаетм кдаужю бкуву по отдльенотси, а все солво цлиеком.
    "По рзтаьуеазтлм иеалводссинй огдноо аийоглнксго уеириетстнва, не иеемт зичаення, в ккаом пкоядре рснлаепожоы бувкы в солве. Гнвлоае, чтбоы пвраея и плдсонеяя бкувы были на метсе. оаслынтье бвкуы мгоут свлоеатдь в полном бспокдярее, все-равно тскет чиаттсея без полебрм. Пичоинрй эотго ятлсевяя то, что мы не чатеим кжудаю бквуу по онлотдестьи, а все слово цоелким.
    
