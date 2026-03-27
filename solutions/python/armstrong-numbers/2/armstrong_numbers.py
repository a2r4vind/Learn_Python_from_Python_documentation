import sys 

def is_armstrong_number(number):
    num_str = str(number)
    num_of_digits = len(num_str)
    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        total += digit ** num_of_digits
        temp //= 10

    return True if total == number else False


        
        
        
    
