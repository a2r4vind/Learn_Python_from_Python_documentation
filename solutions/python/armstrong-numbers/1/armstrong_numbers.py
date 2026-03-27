def is_armstrong_number(number):
    num_str = str(number)
    num_of_digits = len(num_str)
    sum = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        sum += digit ** num_of_digits
        temp //= 10

    if sum == number:
        return True
    else:
        return False
        
        
        
    
