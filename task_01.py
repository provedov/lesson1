import string
def is_palindrome(text):
    if text == None:
        return False
        return
    if isinstance(text,int) == True:
        text = str(text)
    text = text.lower()
    text = clearNullText(text)
    ans = True
    size = len(text)
    for i in range(size):
        if text[i] != text[(-1)*i-1]:
            ans = False
            break
    return ans
def clearNullText(text):
    size = len(text)
    newText = ''
    it = 0
    for i in range(size):
        if text[i] ==' ':           
            newText = newText +text[it:i]
            it = i+1
    newText = newText +text[it:size]    
    text = newText
    newText = '' 
    it = 0
    size = len(text)
    for i in string.punctuation:
        if i in text:
            text = text.replace(i,'')
    return text   
