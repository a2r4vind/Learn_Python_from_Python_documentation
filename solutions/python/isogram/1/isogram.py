def is_isogram(string):

    # convert input string to lower case
    string = string.lower()
    
    input_str = []
    for letter in string:
        if letter not in (' ', '-'):
            input_str.append(letter)

    isogram_list = []
    for letter in input_str:
        if letter not in isogram_list:
            isogram_list.append(letter)

    return input_str == isogram_list
        
