'''
Write a function that accepts a string, and returns true if it is in the form of a phone number. <br/>Assume that any integer from 0-9 in any of the spots will produce a valid phone number.<br/>

Only worry about the following format:<br/>
(123) 456-7890   (don't forget the space after the close parentheses) <br/> <br/>
Examples:

```
"(123) 456-7890"  => true
"(1111)555 2345"  => false
"(098) 123 4567"  => false
```

'''

def valid_phone_number(phone_number):
    num = phone_number
    valid_number = "({}) {}-{}".format(num[1:4], num[6:9], num[10:])

    check = lambda x: x.isnumeric()

    for i in [num[1:4], num[6:9], num[10:]]:
        for j in i:
            if not check(j):
                return False

    return valid_number == num and len(num) == 14