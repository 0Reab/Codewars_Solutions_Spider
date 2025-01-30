'''
# Instructions 

Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (`word`) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

# Example (Input --> Output)

```
"CodEWaRs" --> [0,3,4,6]
```
'''

def capitals(word):
    count = -1
    result = []   

    for i in word:
        count += 1
        
        if i == i.upper():
            result.append(count)
    return result