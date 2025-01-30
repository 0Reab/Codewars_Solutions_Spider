'''
# Write Number in Expanded Form

You will be given a number and you will need to return it as a string in [Expanded Form](https://www.mathsisfun.com/definitions/expanded-notation.html). For example:

```
   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"
```

NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out [part 2](https://www.codewars.com/kata/write-number-in-expanded-form-part-2)!!

'''

def expanded_form(num):
    zero = '0'
    result = '' 
    count = len(str(num)) 
    
    for i in str(num):
        count -= 1
        if i != zero:
            result += f'{i+(zero*count)} + '     
    
    return result[:-3]