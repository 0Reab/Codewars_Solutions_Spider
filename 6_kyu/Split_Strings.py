'''
Complete the solution so that it splits the string into pairs of two characters.  If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
```
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
```

'''

def solution(s):
    result = []
    chars = ""
    count = 0

    while 0 != len(s):
        chars = ""
        count += 1

        try:
            chars = s[0] + s[1]
            s = s[2:]
        except:
            if len(s) != 0:
                chars = s[0] + '_'
                s = s[1:]

        result.append(chars)

    return result