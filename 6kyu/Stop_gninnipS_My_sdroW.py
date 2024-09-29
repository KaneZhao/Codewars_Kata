def spin_words(sentence):
    # Your code goes here
    if sentence is None or len(sentence) <= 1:
        return sentence
    lst = sentence.split(' ')
    for i in range(len(lst)):
        if len(lst[i]) >= 5:
            lst[i] = lst[i][::-1]            
    return ' '.join(lst)