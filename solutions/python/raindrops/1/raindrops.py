def convert(number):
    '''
    function than convert the given number to its corresponding raindrop sounds.
    '''

    result = ""

    if number % 105 == 0 :
        result += "PlingPlangPlong"
    elif number % 3 == 0:
        result += "Pling"
        if number % 5 == 0:
            result += "Plang"
        elif number % 7 == 0:
            result += "Plong"
    elif number % 5 == 0:
        result += "Plang"
        if number % 7 == 0:
            result += "Plong"
    elif number % 7 == 0:
        result += "Plong"
    else:
        result += str(number)

    return result