def max_odd(array = None):
    if array == None:
        return array
    array_odd = None
    size = len(array)
    maxnum = None
    for i in range(size):
        if((isinstance(array[i],int) == True or isinstance(array[i],float) == True)):
            if(array[i]%2 != 0 and maxnum == None):
                maxnum = int(array[i])
            elif array[i]%2 != 0 and maxnum < array[i]:
                maxnum = int(array[i])
    return maxnum
