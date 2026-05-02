def score(x, y):
    '''
    Function to calculate the score of Dart game.
    '''
    score = 0
    distance = (x**2 + y**2) ** (0.5)

    if 0 <= distance <= 1:
        score += 10
    elif 1 < distance <= 5:
        score += 5
    elif 5 < distance <= 10:
        score += 1

    return score
