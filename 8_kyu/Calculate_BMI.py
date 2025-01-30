'''
Write function bmi that calculates body mass index (bmi = weight / height<sup>2</sup>).


if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

'''

def bmi(weight, height):
    bmi = weight / (height**2)
    
    if bmi > 30:
        return "Obese"
    
    elif bmi <= 18.5:
        return "Underweight"
    
    elif bmi <= 25.0:
        return "Normal"
    
    else:
        return "Overweight"
