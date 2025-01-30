'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

### Examples (input --> output):
```
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
```
'''

def rgb(r,g,b):

    dic = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

    result = []

    for i in [r,g,b]:
        count = 0

        if i <= 0:
            result.append("0")
            result.append("0")

        if i > 255:
            i -= i
            result.append(dic[15])
            result.append(dic[15])

        elif i > 0:
            while i >= 16:
                i -= 16
                count += 1

            result.append(dic[count])
            result.append(dic[i])
            
    return ''.join(result)