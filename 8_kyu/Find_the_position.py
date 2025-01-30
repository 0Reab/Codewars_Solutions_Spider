'''
When provided with a letter, return its position in the alphabet.

Input :: "a"

Output :: "Position of alphabet: 1"


**Note: Only lowercased English letters are tested**

'''

def position(alphabet):
    return f'Position of alphabet: {ord(alphabet)-96}'