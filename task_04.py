def sort_list(array):
    if array == None or array == []:
        array = []
        return array
    array = sorted(array)
    rev = [];
    for i in reversed(array):
        rev.append(i);
    rev.append(rev[-1])
    return rev
