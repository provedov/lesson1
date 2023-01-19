def coincidence(array = None,al = None):
    if array == None or al == None:
        print('[]')
        return
    size = len(array)
    a = '['
    for i in range(size):
        if((isinstance(array[i],int) == True or isinstance(array[i],float) == True)):
            if (array[i] <= max(al) and array[i] >= min(al)):
                a = a + str(array[i])
                if(i!= size):
                    a = a + ', '
    
    print(a[0:-2]+']')
