'''
Build Tower
---

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer `number of floors`. A tower block is represented with `"*"` character.

For example, a tower with `3` floors looks like this:

```
[
  "  *  ",
  " *** ", 
  "*****"
]
```

And a tower with `6` floors looks like this:

```
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
```

___

Go challenge [Build Tower Advanced](https://www.codewars.com/kata/57675f3dedc6f728ee000256) once you have finished this :)

'''

def tower_builder(n_floors):
    char='*'
    count=1
    space=" "
    cdown=n_floors-1
    arr = []
    
    for i in range(n_floors):

        arr.append((space*cdown) + (char*count) + (space*cdown))

        count+=2
        cdown-=1
    
    return arr