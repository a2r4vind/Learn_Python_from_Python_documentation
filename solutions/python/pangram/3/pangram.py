def is_pangram(sentence):

    # convert given sentence into lowercase.
    sentence_in_lowercase = sentence.lower()

    # hashmap
    alphabets_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 
                      'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
                      'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
                      'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
                      'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
                      'z': 0}

    for alpha in sentence_in_lowercase:
        # check if alpha present in sentence is also present in alphabets_count
        if alpha in alphabets_count:
            alphabets_count[alpha] += 1

    return 0 not in alphabets_count.values() 
    
    