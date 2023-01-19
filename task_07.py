def combine_anagrams(words_array):
    size = len(words_array)
    list_of_anagrams = []
    word = ''
    for i in range(size):
        if words_array[i]!='':
            module = [words_array[i]]
        else:
            continue
        for y in range(size):
            if words_array[i] != words_array[y] and words_array[i] !=''and words_array[y] !='':
                if words_is_anagram(words_array[i],words_array[y]) == True:
                    module.append(words_array[y])
                    words_array[y] = ''
        list_of_anagrams.append(module)        
        words_array[i] = ''
    print(list_of_anagrams)
def words_is_anagram(word_1,word_2):
    size = len(word_1)     
    for i in word_1:
        if word_2.find(i) == -1:
            return False
    for i in word_2:
        if word_1.find(i) == -1:
            return False
    return True
