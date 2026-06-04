def label(colors):
    
    color_to_value_mapping = {
        "black": "0",
       "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9"
    }


    ohms = ""
    zeros_count = 0
    black_count = 0
    prefix = None
    for index, color in enumerate(colors):
        
        if index == 2 and black_count != 2: # when starting 2 colors were not the same black color
            
            if color == "black": # when last color is black no zeros are added
                break 
                
            num_of_zeros = "0" * int(color_to_value_mapping[color])
            
            ohms = ohms + num_of_zeros

            # when 2nd color is black (0) and last color is red (2) or 3 <= num of zeros < 6
            if (zeros_count == 1 and len(num_of_zeros) == 2 ) or (3 <= len(num_of_zeros) < 6):
                prefix = " kiloohms"
                ohms = ohms[:-3]
                break

            # when 6 <= num of zeros < 9
            if 6 <= len(num_of_zeros) < 9:
                prefix = " megaohms"
                ohms = ohms[:-6]
                break

            # when 9 <= num of zeros
            if len(num_of_zeros) >= 9:
                prefix = " gigaohms"
                ohms = ohms[:-9]
                break
                
            break 

        if index == 0 and color == "black":
            black_count += 1 # for the edge case of '00'
            continue 
            
        if index == 1 and color == "black":
            zeros_count += 1 # for the edge case of any num + 0 at its 2nd place
            black_count += 1 # for the edge case of '00'
            if black_count == 2:
                continue
            
        ohms = ohms + color_to_value_mapping[color] # ohms value from color

    if prefix is None:
        ohms_value = ohms + " ohms"  # when no prefix is added to ohms
    else:
        ohms_value = ohms + prefix # when needed to add prefix to ohms

    return ohms_value