def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquot_sum = 0

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        for divisor in range(1, number):
            if number % divisor == 0:
                aliquot_sum += divisor
    
        if aliquot_sum == number:
            label = "perfect"
        elif aliquot_sum > number:
            label = "abundant"
        else:
            label = "deficient"
    
        return label

