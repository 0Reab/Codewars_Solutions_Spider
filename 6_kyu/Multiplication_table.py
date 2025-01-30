'''
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given `size` is 3:
```
1 2 3
2 4 6
3 6 9
```

For the given example, the return value should be: 

```js
[[1,2,3],[2,4,6],[3,6,9]]
```
```julia
[1 2 3; 2 4 6; 3 6 9]
```

```if:c
Note: in C, you must return an allocated table of allocated rows
```

'''

def multiplication_table(size):
    count = 1

    arr_one = [a+1 for a in range(size)]

    final=[]
    tmp = []

    for i in range(size):
        for i in arr_one:
            tmp.append(i*count)
        count+=1
        final.append(tmp[-size:])

    return final