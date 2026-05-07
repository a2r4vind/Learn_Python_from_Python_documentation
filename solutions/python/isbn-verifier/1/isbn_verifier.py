def is_valid(isbn):

    # create list of digits in isbn
    digits = [digit for digit in isbn if digit.isalnum()]

    # check if length of given isbn is 10
    if len(digits) != 10:
        return False
    
    total = 0
    multiplier = 10
    for digit in digits:
        if digit not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X'):
            return False
        else:
            if digit == 'X':
                if digits[-1] != digit:
                    return False
                digit = 10
            total += int(digit) * multiplier
        multiplier -= 1

    return total % 11 == 0
    
