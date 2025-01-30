'''
Write a function which converts the input string to uppercase.

~~~if:bf
For BF all inputs end with \0, all inputs are lowercases and there is no space between.
~~~

~~~if:riscv
RISC-V: The function signature is

```c
void to_upper_case(const char *str, char *out);
```

`str` is the input string. Write your result to `out`. You may assume it is large enough to hold the result. You do not need to return anything.
~~~

'''

def make_upper_case(s):
    return s.upper()
