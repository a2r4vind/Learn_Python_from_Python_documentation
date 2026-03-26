def equilateral(sides):
    s1, s2, s3 = sides

    if s1 > 0 and s2 > 0 and s3 > 0:
        
            if s1 == s2 == s3:
                return True
            
    return False


def isosceles(sides):
    s1, s2, s3 = sides

    if s1 > 0 and s2 > 0 and s3 > 0:
        if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
            if  equilateral(sides):
                return True
            elif s1 == s2 or s1 == s3 or s2 == s3:
                return True
                
    return False


    
def scalene(sides):
    s1, s2, s3 = sides

    if s1 > 0 and s2 > 0 and s3 > 0:
        if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
            if not equilateral(sides) and not isosceles(sides):
                return True
    
    return False
