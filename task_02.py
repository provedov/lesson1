def coincidence(array = None,al = None):
    if array == None or al == None:
        array = []
        return array
    size = len(array)
    a = []
    for i in range(size):
        if((isinstance(array[i],int) == True or isinstance(array[i],float) == True)):
            if (array[i] <= max(al) and array[i] >= min(al)):
                a.append(array[i])                 
    return a
