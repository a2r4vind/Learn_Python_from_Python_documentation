def translate(text):
    '''Function defined to translate english text into Pig Latin
    
    param: text: str - The English text
    return: str - pig-latin text
    '''

    vowels = ['a','e','i','o','u']
    words = text.split()
    result = []

    for word in words:

        # Rule 1
        if word[0] in vowels or word[:2] in ('xr', 'yt'):
            new_text = word[:] + 'ay'
            result.append(new_text)
            break
            

        for i in range(len(text)):

            # Rule 3
            if word[i:i+2] == 'qu':
                if i == 0:
                    new_text = word[i+2:] + 'qu' + 'ay'
                else:
                    new_text = word[i+2:] + word[:i] + 'qu' + 'ay'
                result.append(new_text)
                break

            # Rule 2 + Rule 4
            if i != 0 and (word[i] in vowels or word[i] == 'y'):
                new_text = word[i:] + word[:i] + 'ay'
                result.append(new_text)
                break

    return ' '.join(result)

            


    
