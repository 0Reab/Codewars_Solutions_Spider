'''
You are given two interior angles (in degrees) of a triangle. 

Write a function to return the 3rd.

Note: only positive integers will be tested.

https://en.wikipedia.org/wiki/Triangle
'''

a=$1
b=$2
calculate() {
  sum=$(( (($a + $b) - 180) ))
  sum=$(($sum*-1))
  echo $sum
}

calculate $a $b