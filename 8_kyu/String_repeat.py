'''
~~~if:bf
Write a program which accepts a single byte `n` and then a sequence of bytes `string` and outputs the `string` exactly `n` times.

The first input byte will be `n`. Following bytes will be characters of `string`. The end of the input `string` will be indicated with a null byte `\0`.

### Examples:

"\6I" -> "IIIIII"
"\5Hello" -> "HelloHelloHelloHelloHello"
~~~

Write a function that accepts an integer `n` and a string `s` as parameters, and returns a string of `s` repeated exactly `n` times.

### Examples (input -> output)

```
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
```

'''

def repeat_str(repeat, string):
    result = ''
    for i in range(repeat):
        result += string
    return result