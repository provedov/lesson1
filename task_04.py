def sort_list(array):
    if array == None or array == []:
        array = []
        return array
    minNum = min(array)
    maxNum = max(array)
    size = len(array)
    for i in range(size):
        if array[i] == maxNum:
            array[i] = minNum
        elif array[i] == minNum:
            array[i] = maxNum   
    array.append(minNum)
    return array
