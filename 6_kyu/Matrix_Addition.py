'''
Write a function that accepts two square matrices (`N x N` two dimensional arrays), and return the sum of the two. Both matrices being passed into the function will be of size `N x N` (square), containing only integers.

How to sum two matrices:

Take each cell `[n][m]` from the first matrix, and add it with the same `[n][m]` cell from the second matrix. This will be cell `[n][m]` of the solution matrix. (Except for C where solution matrix will be a 1d pseudo-multidimensional array).

Visualization: 
```
|1 2 3|     |2 2 1|     |1+2 2+2 3+1|     |3 4 4|
|3 2 1|  +  |3 2 3|  =  |3+3 2+2 1+3|  =  |6 4 4|
|1 1 1|     |1 1 3|     |1+1 1+1 1+3|     |2 2 4|
```

## Example
```javascript
matrixAddition(
  [ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ],
//      +
  [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ] )

// returns:
  [ [3, 4, 4],
    [6, 4, 4],
    [2, 2, 4] ]
```

'''

from itertools import chain

def matrix_addition(a, b):
    result = []
    chain_one, chain_two = list(chain.from_iterable(a)), list(chain.from_iterable(b)) # flatten to 1D array
    length = len(a[0])
    summed = list(reversed([ num + chain_two[idx] for idx, num in enumerate(chain_one) ])) # sum 1D arrays

    for i in summed: # construct summed 1D to 2D array
        tmp = []
        for _ in range(length):
            tmp.append(summed.pop())
        result.append(tmp)

    return result