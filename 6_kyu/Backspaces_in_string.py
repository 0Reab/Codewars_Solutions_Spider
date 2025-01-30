'''
Assume `"#"` is like a backspace in string. This means that string `"a#bc#d"` actually is `"bd"`

Your task is to process a string with `"#"` symbols.


## Examples

```
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
```
'''

def clean_string(s):
    stk = [] # stack

    for c in s: # for char in
        if stk and c=='#': stk.pop() # pop 
        elif c != '#': stk.append(c) # push 

    return ''.join(stk) # format
