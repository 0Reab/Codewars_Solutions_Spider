'''
Find the total sum of internal angles (in degrees) in an n-sided simple polygon. N will be greater than 2.
'''

def angle(n):
    result = 0
    
    for i in range(3,n+1):
        result += 180
        
    return result