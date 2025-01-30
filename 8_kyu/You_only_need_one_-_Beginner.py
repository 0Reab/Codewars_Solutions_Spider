'''
You will be given an array `a` and a value `x`. All you need to do is check whether the provided array contains the value.

~~~if:swift
The type of `a` and `x` can be `String` or `Int`.
~~~
~~~if-not:swift
`a` can contain numbers or strings. `x` can be either.
~~~
~~~if:racket
In racket, you'll be given a list instead of an array. If the value is in the list,
return #t instead of another value that is also considered true.
```racket
(contains '(1 2 3) 3) ; returns #t
(contains '(1 2 3) 5) ; returns #f
```
~~~

Return `true` if the array contains the value, `false` if not. 
'''

def check(seq, elem):
    for i in seq:

        if i == elem:
            return True
    return False