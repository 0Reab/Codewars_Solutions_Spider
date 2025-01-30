'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

**Note: input will never be an empty string**

'''

def fake_bin(x):
    lst = [ 0 if int(number) < 5 else 1 for number in x ]
    
    return ''.join(map(str,lst))
    