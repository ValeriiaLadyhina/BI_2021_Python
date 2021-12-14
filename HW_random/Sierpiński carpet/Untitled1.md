```python
import random as rd
import matplotlib.pyplot as plt
```


```python
def carpet_sierpinski():
    resultx = []
    resulty = []
    points = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    start = rd.choice(points)
    resultx.append(start[0])
    resulty.append(start[1])
    plt.figure(figsize=(10, 10))
    plt.scatter(start[0], start[1])
    for i in range(1000000):
        addition = rd.choice(points)
        start = [(start[0]+2*addition[0])/3,(start[1]+2*addition[1])/3]
        resultx.append(start[0])
        resulty.append(start[1])
    plt.scatter(resultx, resulty, c='b', s=2)
    plt.title('Sierpinski carpet')
carpet_sierpinski()
```


    
![png](output_1_0.png)
    



```python

```
