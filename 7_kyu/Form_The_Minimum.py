'''
### Task

Given a list of digits, return the **smallest number** that could be formed from these digits, using the digits only once (ignore duplicates). **Only positive integers** in the range of 1 to 9 will be passed to the function.

### Examples 

```
[1, 3, 1] ==> 13
[5, 7, 5, 9, 7] ==> 579
[1, 9, 3, 1, 7, 4, 6, 6, 7]  ==> 134679
```
___

[Playing with Numbers Series](https://www.codewars.com/collections/playing-with-numbers)

[Playing With Lists/Arrays Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)

[Bizarre Sorting-katas](https://www.codewars.com/collections/bizarre-sorting-katas)

[For More Enjoyable Katas](http://www.codewars.com/users/MrZizoScream/authored)
'''

def min_value(digits):
    return int(''.join(str(i) for i in sorted(set(digits))))