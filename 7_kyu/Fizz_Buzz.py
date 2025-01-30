'''
~~~if-not:scala
Return an array containing the numbers from 1 to N, where N is the parametered value.
~~~

~~~if:scala
Return a list containing the numbers from 1 to N, where N is the parametered value.
~~~

Replace certain values however if any of the following conditions are met:
* If the value is a multiple of 3: use the value "Fizz" instead
* If the value is a multiple of 5: use the value "Buzz" instead
* If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead

N will never be less than 1.

Method calling example:
```python
fizzbuzz(3) -->  [1, 2, "Fizz"]
```
```haskell
fizzbuzz(3) -->  ["1", "2", "Fizz"]
```
```kotlin
fizzBuzz(3) -->  ["1", "2", "Fizz"]
```
```csharp
string[] result = FizzBuzz.GetFizzBuzzArray(3); // => [ "1", "2", "Fizz" ]
```
```prolog
fizzify(3, [1, 2, "Fizz"]).
```
```scala
FizzBuzz.fizzify(3) // List("1", "2", "Fizz")
```
```java
FizzBuzzArray.fizzBuzz(3) -->  ["1", "2", "Fizz"]
```

'''

def fizzbuzz(n):
    lst = []
    
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            lst.append('FizzBuzz')
        elif i%3 == 0:
            lst.append('Fizz')
        elif i%5 == 0:
            lst.append('Buzz')
        elif i%3 != 0 and i%5 != 0: 
            lst.append(i)
            
    return lst