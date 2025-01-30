'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns `"now"`. Otherwise,  the duration is expressed as a combination of `years`, `days`, `hours`, `minutes` and `seconds`.

It is much easier to understand with an example:

```text
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
```

**For the purpose of this Kata, a year is 365 days and a day is 24 hours.**

Note that spaces are important.


### Detailed rules

The resulting expression is made of components like `4 seconds`, `1 year`, etc.  In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (`", "`). Except the last component, which is separated by `" and "`, just like it would be written in English. 

A more significant units of time will occur before than a least significant one. Therefore, `1 second and 1 year` is not correct, but `1 year and 1 second` is.

Different components have different unit of times. So there is not repeated units like in `5 seconds and 1 second`.

A component will not appear at all if its value happens to be zero.  Hence, `1 minute and 0 seconds` is not valid, but it should be just `1 minute`.

 A unit of time must be used "as much as possible". It means that the function should not return `61 seconds`, but `1 minute and 1 second` instead.  Formally, the duration specified by  of a component must not be greater than any valid more significant unit of time.

'''

def format_duration(sec):
    result = {"year": 0, "day": 0, "hour": 0, "minute": 0, "second": 0} # for incrementing time in units 
    calc = {"year": (86_400*365), "day": 86_400, "hour": 3600, "minute": 60} # to loop over and calculate via subtract func
    output = '' # final formated output sentence
    
    def subtract(time, unit, sec, result):
    # using sec, subtract it from greatest unit in calc to smallest
        if sec >= time:
            sec -= time # decrement global sec
            result[unit] += 1 # increment result dict
        return sec
    
    
    while sec > 0:
        # until 0 sec run subtract func
        for k, v in calc.items(): # process all units except seconds
            sec = subtract(v, k, sec, result)
                
        if sec < 60: # process seconds
            result["second"] += sec
            sec -= sec
            
    def convert(fro, to, val, result):
        # function to convert 70 min to: 1h and 10min etc...
        while result[fro] >= val:
            result[to] += 1
            result[fro] -= val
            
    # run convert function  
    convert("minute", "hour", 60, result)  
    convert("hour", "day", 24, result)
    

    for unit, val in result.items():
        # make a formated output string
        if val > 0:
            plural = 's'
            if val == 1:
                plural = ''
            # add plural support for units: second/seconds
            output += f'{str(val)} {unit}{plural}, '

    output = output[:-2] # remove extra chars ', '

    if output == '':
        # account for 0 time
        output = 'now'

    if len(output.split(',')) > 1:
        # formatting into sentence
        last = output.split(',')[-1]
        output = ','.join(output.split(',')[0:-1])
        output += f' and{last}'
        
    return output