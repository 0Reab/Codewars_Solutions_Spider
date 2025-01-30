'''
Complete the solution so that the function will break up camel casing, using a space between words.

### Example 

```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```
'''

def solution(s):
    return ''.join([' '+i if i == i.upper() else i for i in s])