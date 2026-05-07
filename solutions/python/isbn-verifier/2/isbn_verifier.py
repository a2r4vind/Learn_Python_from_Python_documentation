def is_valid(isbn):
        
    total = 0
    multiplier = 10
    digit_count = 0
    
    for char in isbn:
        digit_count += 1
        if char == "-":
            digit_count -= 1
            continue 
        elif char == "X" and multiplier == 1:
            total += 10
            multiplier -= 1
        elif char.isdigit():
            total += int(char) * multiplier
            multiplier -= 1

    return digit_count == 10 and multiplier == 0 and total % 11 == 0
            
    
