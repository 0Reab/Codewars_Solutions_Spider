'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.

## Examples

```
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
```

'''

def find_outlier(integers):
    even_count = 0
    odd_count = 0
    
    for num in integers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    outlier_parity = 'even' if even_count > odd_count else 'odd'
    
    for num in integers:
        if outlier_parity == 'even' and num % 2 != 0:
            return num
        elif outlier_parity == 'odd' and num % 2 == 0:
            return num