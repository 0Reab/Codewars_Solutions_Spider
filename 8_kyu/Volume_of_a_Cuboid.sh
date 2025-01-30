'''
Bob needs a fast way to calculate the volume of a cuboid with three values: the `length`, `width` and `height` of the cuboid. Write a function to help Bob with this calculation.

```if:shell
In bash the script is ran with the following 3 arguments:
`length` `width` `height`
```

'''

#!/bin/bash
length=$1
width=$2
height=$3
result=$(echo "$length * $width * $height" | bc -l)
echo $result