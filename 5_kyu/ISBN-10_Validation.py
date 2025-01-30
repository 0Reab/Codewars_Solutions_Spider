'''
ISBN-10 identifiers are ten digits long. The first nine characters are digits `0-9`. The last digit can be `0-9` or `X`, to indicate a value of 10.

An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

For example:
```
ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
```
This is a valid ISBN, because:
```
(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
```


## Examples

```
1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false
```
'''

def valid_ISBN10(isbn: []):
    valid_nums = '0123456789'
    count = 1
    sum = 0

    # Poor man's regex for numbers and x
    if len(isbn) != 10 or isbn[9] not in valid_nums+'X' or len([i for i in isbn[:8] if i not in valid_nums]) > 0: return False

    # Now calculate validity based on reqs
    for i in isbn:
        if i == 'X':
            sum += 100
        else:
            sum += int(i) * count

        count += 1

    return sum % 11 == 0