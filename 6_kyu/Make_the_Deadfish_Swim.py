'''
Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to 0.

It uses four single-character commands:
- `i`: Increment the value
- `d`: Decrement the value
- `s`: Square the value
- `o`: Output the value to a result array

All other instructions are no-ops and have no effect.

## Examples

Program `"iiisdoso"` should return numbers `[8, 64]`.  
Program `"iiisdosodddddiso"` should return numbers `[8, 64, 3600]`.

'''

def parse(data):
    lst = []
    start = 0
    for cmd in data:
        match cmd:
            case 'i':
                start += 1
            case 'd':
                start -= 1
            case 's':
                start = start**2
            case 'o':
                lst.append(start)
    return lst