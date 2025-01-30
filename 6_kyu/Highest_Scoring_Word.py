'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: `a = 1, b = 2, c = 3` etc.

For example, the score of `abad` is `8` (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

def high(x):
    abcs = {}
    scores = {} 
    
    for i in range(1,24):
        i += 96
        abcs[chr(i)] = i 
    
    for word in x.split():
        scores[word] = 0
        tmp = 0
        
        for char in word:
            tmp += ord(char) - 96
            
        scores[word] += tmp
    
    return max(scores, key=scores.get)