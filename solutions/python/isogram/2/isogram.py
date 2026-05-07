def is_isogram(string):

    # convert letter of the string to lowercase and append only alphabets of the string 
    letters_in_string = [letter.lower() for letter in string if letter.isalpha()]

    # check if length of letters_in_string list is equal to length of set(letters_in_string)
    return len(letters_in_string) == len(set(letters_in_string))

    

        
