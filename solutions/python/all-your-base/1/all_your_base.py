def rebase(input_base, digits, output_base):

    # check input_base >= 2
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # check output_base >= 2
    if output_base < 2:
        raise ValueError("output base must be >= 2")
        
    decimal_number = 0

    # calculate decimal number from given input base and list of digits
    for power, digit in enumerate(digits[::-1]):
        if 0 <= digit < input_base:
            decimal_number += digit * (input_base ** power)
        else:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # check if decimal_number is zero
    if decimal_number == 0:
        return [0]

    output_list = []
    temp_num = decimal_number
    while temp_num > 0:
        remainder = temp_num % output_base
        output_list.append(remainder)
        temp_num //= output_base
    
    return output_list[::-1]
