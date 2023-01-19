def sort_list(array):
    if array == None:
        print('[]');
        return
    array = sorted(array)
    rev = [];
    for i in reversed(array):
        rev.append(i);
    rev.append(rev[-1])
    print(rev)
