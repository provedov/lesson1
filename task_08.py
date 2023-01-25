def multiply_numbers(inputs = None):
    if inputs == None:
        return None
    a = 1    
    if isinstance(inputs,str) == True:
        if ExistNumbers(inputs) == False:
            return None
        for i in inputs:
            if isNumber(i) == True:
                a *= int(i)
        return a
    if isinstance(inputs,float) == True:
        inputs = str(inputs)
        for i in inputs:
            if isNumber(i) == True:
                a *= int(i)
        return a
    if isinstance(inputs,list) == True:
        for i in inputs:
            a*= i
        return a
def isNumber(Num):
    for i in range(0,10):
        if Num == str(i):
            return True
    return False
def ExistNumbers(inputs):
    for i in inputs:
        if isNumber(i) == True:
            return True
    return False
        
        
    
