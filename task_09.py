def connect_dicts(dict1, dict2):
    if(isinstance(dict1,dict)!= 1 or isinstance(dict2,dict) != 1):
        print('Ошибка')
        return
    count_dict1 = 0
    count_dict2 = 0
    for i in dict1:
        count_dict1 = count_dict1 + dict1[i]
    for i in dict2:
        count_dict2 = count_dict2 + dict2[i]
    print(count_dict1)
    print(count_dict2)
    del_dict = {}
    for i in dict1:
        if dict1[i] < 10:
            del_dict[i] = dict1[i]
    for i in del_dict:
        del dict1[i]
    del_dict = {}
    for i in dict2:
         if dict2[i] < 10:
             del_dict[i] = dict2[i]
    for i in del_dict:
        del dict2[i]   
    new_dict={}
    for i in dict1:
        new_dict[i] = dict1[i]
    for i in dict2:
        if i in new_dict and count_dict1 <= count_dict2:
            new_dict[i] = dict2[i]        
        elif not i in new_dict:
            print(i)
            new_dict[i] = dict2[i]
    sorted_dict = dict(sorted(new_dict.items(), key=lambda item: item[1]))
    print(dict1)
    print(dict2)
    print(sorted_dict)
