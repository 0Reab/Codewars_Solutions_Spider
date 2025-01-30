'''
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
```if:java
For Java, those integers will come as double precision (long).
```
For example, when an array is passed like `[19, 5, 42, 2, 77]`, the output should be `7`.

`[10, 343445353, 3453445, 3453545353453]` should return `3453455`.

'''

def sum_two_smallest_numbers(numbers):
    x = min(numbers)
    lst = []
    for i in numbers:
        if i > x:
            lst.append(i)
    y = min(lst)
    return x+y