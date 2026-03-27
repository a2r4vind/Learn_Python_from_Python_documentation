def square(number):
    """Function that return number of grains on a given square number of a chess board

    para: number: int - square number on chess board.
    return: int or error
    """
    
    if 0 < number <= 64:
        if number == 1:
            return 1
        return 2 * square(number - 1)
    else:
        raise ValueError('square must be between 1 and 64')


def total():
    """Function that return total number of grains on the chessboard.
    """
    
    total = 0

    for sq in range(1, 65):
        total += square(sq)

    return total
    
