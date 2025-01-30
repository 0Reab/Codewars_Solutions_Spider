'''
Create a function taking a positive integer between `1` and `3999` (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.


In Roman numerals:
* `1990` is rendered: `1000`=`M` + `900`=`CM` + `90`=`XC`; resulting in `MCMXC`.
* `2008` is written as `2000`=`MM`, `8`=`VIII`; or `MMVIII`.
* `1666` uses each Roman symbol in descending order: `MDCLXVI`.

Example:
```
   1 -->       "I"
1000 -->       "M"
1666 --> "MDCLXVI"
```

Help:
```
Symbol	Value
I	      1
V	      5
X	      10
L	      50
C	      100
D	      500
M	      1,000
```

[More about roman numerals](https://en.wikipedia.org/wiki/Roman_numerals)
'''


def solution(n):
    sym = {
        1000: "M", 
        900: "CM", 
        500: "D", 
        400: "CD",
        100: "C", 
        90: "XC", 
        50: "L", 
        40: "XL",
        10: "X", 
        9: "IX", 
        5: "V", 
        4: "IV",
        1: "I"
    }
    count = 0
    result = ""

    if n in sym: 
        return sym[n]

    
    digits = (len(str(n)))


    for i in str(n):
        
        count += 1

        digit = i + ("0"*(digits-count))
        
        digit = int(digit)

        if digit in sym:
            result += sym[digit]
        else:        
            for key in sorted(sym.keys(), reverse = True):
                while digit >= key:
                    result += sym[key]
                    digit -= key


    return(result)