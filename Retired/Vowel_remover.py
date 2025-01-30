'''
Create a function called `shortcut` to remove the **lowercase** vowels (`a`, `e`, `i`, `o`, `u` ) in a given string.

## Examples

```python
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"
```

* don't worry about uppercase vowels
* `y` is not considered a vowel for this kata
'''

def shortcut( s ):
    return ''.join([i for i in s if i not in 'aeiou'])