def equilateral(sides):
    """Function that return whether triangle formed by given sides is equilateral triangle or not.
    """
    
    side1, side2, side3 = sides

    if side1 > 0 and side2 > 0 and side3 > 0:
        
        if side1 == side2 == side3:
            return True
            
    return False


def isosceles(sides):
    """Function that return whether triangle formed by given sides is isosceles triangle or not.
    """
    
    side1, side2, side3 = sides

    if side1 > 0 and side2 > 0 and side3 > 0:
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            if  equilateral(sides):
                return True
            elif side1 == side2 or side1 == side3 or side2 == side3:
                return True
                
    return False


    
def scalene(sides):
    """Function that return whether triangle formed by given sides is scalene triangle or not.
    """
    
    side1, side2, side3 = sides

    if side1 > 0 and side2 > 0 and side3 > 0:
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            if not equilateral(sides) and not isosceles(sides):
                return True
    
    return False
