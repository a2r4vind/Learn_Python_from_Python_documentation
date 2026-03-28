def steps(number):
    """Function that returns the number of steps required to reach 1 starting from the given number 'number'.

    para: number: int - The starting number.
    return: total_steps: int - total number of steps requied to reach 1 from number 'number'.
    """

    if number > 0:
        total_steps = 0
        if number == 1:
            return total_steps

        if number % 2 == 0:
            total_steps = steps(number // 2)
            total_steps += 1
        else:
            total_steps = steps(3 * number + 1)
            total_steps += 1

        return total_steps
    
    raise ValueError("Only positive integers are allowed")

    