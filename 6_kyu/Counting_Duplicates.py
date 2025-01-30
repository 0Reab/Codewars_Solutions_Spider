'''
### Count the number of Duplicates

Write a function that will return the count of **distinct case-insensitive** alphabetic characters and numeric digits that occur more than 
once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.


### Example
"abcde" -> 0             `# no characters repeats more than once`  
"aabbcde" -> 2           `# 'a' and 'b'`  
"aabBcde" -> 2           ``# 'a' occurs twice and 'b' twice (`b` and `B`)``  
"indivisibility" -> 1    `# 'i' occurs six times`  
"Indivisibilities" -> 2  `# 'i' occurs seven times and 's' occurs twice`  
"aA11" -> 2              `# 'a' and '1'`  
"ABBA" -> 2              `# 'A' and 'B' each occur twice`

'''

def duplicate_count(text):
    dicc = {}
    
    for i in text:
        i = i.lower()
        
        if i not in dicc:
            dicc[i] = 1
        else:
            dicc[i] += 1
            
    if text == "":
        return 0
    
    count = 0 
    
    for key, val in dicc.items():
        print(key, val)
        if val > 1:
            count += 1
            
    return count