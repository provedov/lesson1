def count_words(word):
    import re
    word_d = re.sub('[!@#$\n-.,]', ' ', word)
    word = word_d.lower().split()
    print(word)
    dict_word = {}
    for i in word:
        dict_word[i]=0
    for i in word:
        if i in dict_word:
            dict_word[i]=dict_word[i] +1
    print(dict_word)
