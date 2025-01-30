'''
For this challenge you will write a script that takes the first argument passed in and returns a list of files in the current directory, filtered by file extension. 

For example, if the following files are in a directory:

```
cat.png
cow.jpg
zebra.png
```

and `png` is passed in as the argument then the following should be returned:

```
cat.png
zebra.png
```

> **Note:** The files will be in the current directory.

'''

ls | grep ".$1"