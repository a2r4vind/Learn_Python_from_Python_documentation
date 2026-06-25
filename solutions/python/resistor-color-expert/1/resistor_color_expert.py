def resistor_label(colors):
    """
    Function provide the resistance value for 1 band resistor, 4 band resistor and 5 band resistor.

    input: 
        colors: list: contains the list of colors

    ouput: str: provide the total resistance value along with the maximum tolerance.
    """

    # Convert color to value
    color_value_mapping = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9",
    }

    # Convert color to tolerance value
    tolerance_band = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    if len(colors) == 1: # For 1 Band resistors
        return '0 ohms'

    elif len(colors) == 4: # For 4 Band resistors

        # get the numbers
        for idx in range(4):
            if idx == 0:
                digit_1 = color_value_mapping[colors[idx]]
            elif idx == 1:
                digit_2 = color_value_mapping[colors[idx]]
            elif idx == 2:
                multiplier = 10 ** int(color_value_mapping[colors[idx]])
            else:
                tolerance = tolerance_band[colors[idx]]

        # Form the number
        number = int(digit_1 + digit_2) * multiplier
        
        # convert the number to its suffix
        if number >= 1000000:
            suffix = ' megaohms'
            number  /= 1000000
            number = str(number) + suffix
            
        elif 1000 <= number < 1000000:
            suffix = ' kiloohms'
            number /= 1000
            
            if str(number)[-1] == '0':
                number = str(number)[: -2]
                number += suffix
            else:
                number = str(number) + suffix
        else:
            suffix = ' ohms'
            number = str(number) + suffix
        

        # output: formatted string
        resistance_value = number + " \u00B1" + tolerance 
        return resistance_value
            
    elif len(colors) == 5: # For 5 Band resistors

        # get the numbers
        for idx in range(5):
            if idx == 0:
                digit_1 = color_value_mapping[colors[idx]]
            elif idx == 1:
                digit_2 = color_value_mapping[colors[idx]]
            elif idx == 2:
                digit_3 = color_value_mapping[colors[idx]]
            elif idx == 3:
                multiplier = 10 ** int(color_value_mapping[colors[idx]])
            else:
                tolerance = tolerance_band[colors[idx]]

        # Form the number
        number = int(digit_1 + digit_2 + digit_3) * multiplier
        
        # convert the number
        if number >= 1000000:
            suffix = ' megaohms'
            number  /= 1000000
            number = str(number) + suffix
        elif 1000 <= number < 1000000:
            suffix = ' kiloohms'
            number /= 1000
            if str(number)[-1] == '0':
                number = str(number)[: -2]
                number += suffix
            else:
                number = str(number) + suffix
        else:
            suffix = ' ohms'
            number = str(number) + suffix
        

        # output: formatted string
        resistance_value = number + " \u00B1" + tolerance 
        return resistance_value


